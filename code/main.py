import board
import adafruit_tcs34725
import lgpio
import time
import cv2
import threading
from ultralytics import YOLO 
from picamera2 import Picamera2 
from gpiozero import AngularServo

# ===============================================================
# CONFIG - valores que puedes ajustar sin tocar el resto
# ===============================================================
MOTOR_PIN  = 18                                      # GPIO del carrusel (servo continuo)
MODELO_PATH = "/home/orbyteens/robotica/modelo/best.pt"  # ruta del modelo YOLO

FRAMES_CONFIRMACION = 5    # cuantos frames seguidos debe ver el mismo material para confirmarlo
CONFIANZA_MINIMA    = 0.5  # confianza minima de YOLO para aceptar una deteccion
STOP_US             = 1500 # pulso neutro del servo (lo detiene)

# Tabla de pasos por material:
# "ida"    = cuantos rojos contar para llegar al destino desde el inicio
# "vuelta" = cuantos rojos contar para volver al inicio desde el destino
MATERIALES = {
    "metal":    {"ida": 3, "vuelta": 1},
    "paper":    {"ida": 2, "vuelta": 2},
    "plastic":  {"ida": 1, "vuelta": 3},
    "none":     {"ida": 0, "vuelta": 0},  # carrusel no se mueve, solo compuerta
}

# ===============================================================
# ESTADO GLOBAL
# ===============================================================
parada_emergencia = False  # se activa con SPACE, detiene todo inmediatamente

# ===============================================================
# GPIO - abrir chip y reclamar pin del carrusel
# ===============================================================
chip = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(chip, MOTOR_PIN)

# ===============================================================
# COMPUERTA - dos servos MG996R controlados por AngularServo
# GPIO23 = Motor1 (compuerta principal)
# GPIO25 = Motor2 (seguro / tapa)
# ===============================================================
def crear_servo(pin):
    return AngularServo(
        pin=pin,
        min_angle=0,
        max_angle=180,
        min_pulse_width=0.0005,
        max_pulse_width=0.0025
    )

try:
    motor1 = crear_servo(23)
    motor2 = crear_servo(25)
    print("Motores compuerta listos.")
except Exception as e:
    print(f"Error motores: {e}")
    exit()

motor1.detach()
motor2.detach()

def mover(nombre, servo, grados):
    if 0 <= grados <= 180:
        servo.angle = grados
        time.sleep(0.8)
        print(f"  [{nombre}] en {grados} grados")
    else:
        print(f"  [{nombre}] Valor fuera de rango (0-180)")

def compuerta_ciclo():
    global parada_emergencia

    mover("Motor2", motor2, 90)
    if parada_emergencia: return False

    mover("Motor1", motor1, 130)
    if parada_emergencia: return False

    print("[COMPUERTA] Esperando 2 segundos...")
    time.sleep(2)

    mover("Motor1", motor1, 0)
    if parada_emergencia: return False

    mover("Motor2", motor2, 0)
    if parada_emergencia: return False

    motor1.detach()
    motor2.detach()
    return True

# ===============================================================
# SENSOR
# ===============================================================
i2c_bus = board.I2C()
sensor  = adafruit_tcs34725.TCS34725(i2c_bus)
sensor.gain             = 60
sensor.integration_time = 50

rojo_actual = 0.0
sensor_lock = threading.Lock()
umbral      = 0.0

def hilo_sensor():
    global rojo_actual
    while True:
        try:
            r, g, b, c = sensor.color_raw
            if c > 10:
                total = r + g + b
                if total > 0:
                    with sensor_lock:
                        rojo_actual = (r / total) * 100
        except Exception:
            pass
        time.sleep(0.02)

threading.Thread(target=hilo_sensor, daemon=True).start()

# ===============================================================
# FUNCIONES BASE
# ===============================================================
def leer_tecla():
    return cv2.waitKey(1) & 0xFF

def revisar_parada():
    global parada_emergencia
    tecla = leer_tecla()
    if tecla == ord(' '):
        parada_emergencia = True
        return "SPACE"
    if tecla == ord('q'):
        return "Q"
    return None

def detener_todo():
    print("\n[EMERGENCIA] Deteniendo todo...")
    for _ in range(30):
        lgpio.gpio_write(chip, MOTOR_PIN, 0)
    motor1.angle = 0
    motor2.angle = 0

# ===============================================================
# CARRUSEL
# ===============================================================
def pulso_carrusel(ancho_us):
    lgpio.gpio_write(chip, MOTOR_PIN, 1)
    time.sleep(ancho_us / 1_000_000)
    lgpio.gpio_write(chip, MOTOR_PIN, 0)
    time.sleep((20000 - ancho_us) / 1_000_000)

def motor_stop():
    for _ in range(20):
        pulso_carrusel(STOP_US)

def mover_rojos(cantidad):
    global parada_emergencia
    inicio      = time.time()
    conteo      = 0
    viendo_rojo = False

    print(f"[GPIO18] Girando... 2s antes de contar ({cantidad} rojo(s))")

    while True:
        evento = revisar_parada()
        if evento == "SPACE":
            motor_stop()
            return False
        if evento == "Q":
            motor_stop()
            raise KeyboardInterrupt

        if parada_emergencia:
            motor_stop()
            return False

        with sensor_lock:
            pr = rojo_actual

        transcurrido = time.time() - inicio

        if transcurrido >= 2.0:
            if pr >= umbral and not viendo_rojo:
                viendo_rojo = True
                conteo += 1
                if conteo >= cantidad:
                    motor_stop()
                    return True
            elif pr < umbral and viendo_rojo:
                viendo_rojo = False

        pulso_carrusel(1200)

# ===============================================================
# YOLO
# ===============================================================
def normalizar(clase):
    if clase is None:
        return None
    return str(clase).strip().lower()

def detectar_clase(results, model):
    boxes = results[0].boxes
    if boxes is None or len(boxes) == 0:
        return None
    conf  = boxes.conf.tolist()
    ids   = boxes.cls.tolist()
    idx   = conf.index(max(conf))
    raw   = model.names[int(ids[idx])]
    return normalizar(raw)

# ===============================================================
# CLASIFICACION
# ===============================================================
def calibrar_umbral():
    global umbral
    muestras = []
    for _ in range(10):
        with sensor_lock:
            muestras.append(rojo_actual)
        time.sleep(0.05)
    rojo_base = sum(muestras) / len(muestras)
    umbral = max(0, rojo_base - 5)

def clasificar(clase):
    global parada_emergencia
    clase = normalizar(clase)

    if clase not in MATERIALES:
        return False

    pasos_ida    = MATERIALES[clase]["ida"]
    pasos_vuelta = MATERIALES[clase]["vuelta"]

    if pasos_ida == 0:
        return compuerta_ciclo()

    calibrar_umbral()

    if not mover_rojos(pasos_ida): return False
    if not compuerta_ciclo(): return False
    if not mover_rojos(pasos_vuelta): return False

    return True

# ===============================================================
# MAIN
# ===============================================================
def main():
    global parada_emergencia, umbral

    print("[SISTEMA] Calibrando sensor...")
    time.sleep(1)

    muestras = []
    for _ in range(10):
        with sensor_lock:
            muestras.append(rojo_actual)
        time.sleep(0.05)

    rojo_base = sum(muestras) / len(muestras)
    umbral = max(0, rojo_base - 5)

    print("[SISTEMA] Cargando modelo YOLO...")
    model = YOLO(MODELO_PATH)

    print("[SISTEMA] Iniciando camara...")
    picam2 = Picamera2(0)
    config = picam2.create_preview_configuration(
        main={"size": (1280, 720), "format": "RGB888"}
    )
    picam2.configure(config)
    picam2.start()
    time.sleep(1)

    cv2.namedWindow("Binnsie", cv2.WINDOW_NORMAL)

    clase_actual = None
    frames       = 0
    bloqueado    = False

    try:
        while True:
            frame   = picam2.capture_array()
            results = model(frame, conf=CONFIANZA_MINIMA, verbose=False)
            vista   = results[0].plot()
            cv2.imshow("Binnsie", vista)

            evento = revisar_parada()
            if evento == "SPACE":
                parada_emergencia = True
                detener_todo()
                break
            if evento == "Q":
                break

            clase = detectar_clase(results, model)

            if bloqueado:
                if clase is None:
                    bloqueado    = False
                    clase_actual = None
                    frames       = 0
                continue

            if clase != clase_actual:
                clase_actual = clase
                frames = 1 if clase else 0
            elif clase:
                frames += 1

            if frames >= FRAMES_CONFIRMACION:
                ok = clasificar(clase)

                if parada_emergencia:
                    detener_todo()
                    break

                if ok:
                    bloqueado = True

                clase_actual = None
                frames       = 0

    except KeyboardInterrupt:
        pass

    finally:
        try:
            picam2.stop()
        except:
            pass
        cv2.destroyAllWindows()
        detener_todo()
        motor1.detach()
        motor2.detach()
        lgpio.gpiochip_close(chip)

if __name__ == "__main__":
    main()
