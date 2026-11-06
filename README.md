# BINNSIE – Sistema inteligente de reciclaje

**BINNSIE by Orbyteens**  
**Concepto central: «El contenedor separa, el estudiante aprende.»**

## ¿Qué es BINNSIE?

BINNSIE es un proyecto estudiantil de innovación tecnológica y sostenibilidad que busca mejorar la separación de residuos y fomentar la cultura del reciclaje en las escuelas de Panamá.

El proyecto explora la integración de inteligencia artificial, electrónica, mecanismos automatizados y herramientas digitales para identificar materiales reciclables y dirigirlos a los compartimentos correspondientes. Al mismo tiempo, busca convertir el proceso de reciclaje en una experiencia educativa y participativa para los estudiantes.

## El problema que buscamos abordar

La separación incorrecta de residuos puede contaminar materiales reciclables y dificultar su aprovechamiento. En muchos entornos escolares, reciclar depende de que cada persona identifique el material y lo deposite en el recipiente adecuado. Esto puede generar errores, especialmente cuando no hay información clara, orientación o sistemas de separación accesibles.

BINNSIE busca explorar una alternativa en la que la tecnología apoye la separación desde el punto de depósito y facilite que los estudiantes aprendan sobre los materiales y el reciclaje.

## Objetivo del proyecto

Desarrollar y evaluar una estación inteligente de reciclaje para entornos escolares que combine identificación automatizada de materiales, separación física y recursos educativos para promover mejores prácticas de reciclaje.

### Objetivos específicos

- Explorar el uso de visión artificial para identificar materiales reciclables.
- Diseñar un mecanismo que dirija los materiales identificados a compartimentos correspondientes.
- Investigar formas de ofrecer retroalimentación educativa inmediata a los estudiantes.
- Explorar herramientas digitales que fomenten la participación y el seguimiento de la actividad de reciclaje.
- Evaluar el funcionamiento del sistema y detectar oportunidades de mejora en condiciones reales.

## ¿Cómo funciona el concepto?

La arquitectura conceptual de BINNSIE contempla cuatro componentes:

1. **Identificación mediante cámara e inteligencia artificial.** Una cámara captura una imagen del objeto y un modelo de visión artificial intenta reconocer el material.
2. **Separación automatizada.** A partir de la identificación, el sistema busca accionar un mecanismo que dirija el objeto al compartimento correspondiente.
3. **Retroalimentación inmediata en la estación.** Se planea incorporar una pantalla física para mostrar al estudiante información sobre el material identificado y mensajes educativos. Esta funcionalidad todavía no está desarrollada ni integrada.
4. **Herramienta digital complementaria.** Existe un prototipo experimental de aplicación para explorar la interacción, la gamificación y la acumulación de puntos. No debe considerarse todavía una aplicación final ni una integración completa con el hardware.

## Estado actual del proyecto

BINNSIE se encuentra en una etapa de prototipado y desarrollo experimental.

### Prototipo físico

El equipo construyó un prototipo físico de tamaño grande que utiliza una Raspberry Pi 5. El prototipo permite explorar la integración de la cámara, la inteligencia artificial y el mecanismo físico dentro de un mismo flujo de funcionamiento.

El prototipo actual presenta limitaciones que deben mejorarse, entre ellas su tamaño, la dificultad para transportarlo y la velocidad del proceso de clasificación. El diseño y el funcionamiento continúan en desarrollo.

El programa que se ejecuta en la Raspberry Pi integra la cámara, el modelo de IA y el mecanismo físico. El código correspondiente se incorporará al repositorio cuando esté disponible para revisión y publicación.

### Modelo de inteligencia artificial

El proyecto cuenta con un modelo de detección de objetos basado en YOLOv8. Actualmente, las clases contempladas son:

- Metal
- Paper
- Plastic

El dataset fue organizado y etiquetado utilizando Roboflow, y el entrenamiento del modelo se realizó en Google Colab.

El modelo todavía requiere evaluación, pruebas en condiciones reales y optimización para su uso en la Raspberry Pi 5. Los resultados experimentales no deben interpretarse como una garantía de precisión en un entorno escolar.

### Dataset

BINNSIE utiliza un conjunto de imágenes para entrenar y evaluar el modelo de visión artificial. La organización, calidad de las anotaciones, distribución de las clases, posibles duplicados y condiciones de uso de las imágenes son aspectos que deben revisarse y documentarse.

Antes de publicar o incorporar nuevas imágenes, se deben comprobar los derechos de uso, las licencias aplicables y la ausencia de información personal o sensible.

### Modelo 3D en Tinkercad

El equipo elaboró un modelo 3D en Tinkercad como guía visual para orientar la construcción física del prototipo y la distribución general de sus componentes.

Este modelo fue desarrollado dentro del equipo mientras aprendíamos a utilizar la herramienta. Por lo tanto, es una representación aproximada del prototipo real: puede contener simplificaciones e imperfecciones y **no constituye un diseño CAD profesional ni un plano técnico definitivo para fabricación**.

### Aplicación experimental

Existe un prototipo de aplicación desarrollado con Lovable y Supabase para explorar conceptos de interacción, gamificación y acumulación de puntos.

Puede consultarse aquí: [https://orbyteens.lovable.app/](https://orbyteens.lovable.app/)

La aplicación es experimental. No debe asumirse que está completamente integrada con el prototipo físico, la Raspberry Pi o el modelo de inteligencia artificial.

### Pantalla de retroalimentación

Como parte de la evolución del proyecto, se contempla incorporar una pantalla directamente en la estación. La intención es que los estudiantes reciban retroalimentación sin depender de la aplicación, por ejemplo, información sobre el material identificado o mensajes breves que refuercen el aprendizaje.

Esta función es una propuesta futura y todavía no está implementada.

## Tecnologías y herramientas

| Tecnología o herramienta | Uso dentro del proyecto |
|---|---|
| Raspberry Pi 5 | Plataforma de computación del prototipo físico |
| Python | Desarrollo del programa que integra los componentes del sistema |
| YOLOv8 | Modelo de visión artificial para detección de materiales |
| Roboflow | Organización y anotación del dataset |
| Google Colab | Entorno utilizado para entrenar el modelo |
| Lovable | Desarrollo del prototipo experimental de aplicación |
| Supabase | Backend utilizado por el prototipo de aplicación |
| Tinkercad | Modelado 3D conceptual utilizado como guía para la construcción |

## Limitaciones y desafíos actuales

- Mejorar el tamaño y la facilidad de transporte del prototipo físico.
- Aumentar la velocidad y consistencia del mecanismo de clasificación.
- Evaluar el modelo de IA con objetos, iluminación, ángulos y condiciones variadas.
- Optimizar la ejecución del modelo para Raspberry Pi 5 y comprobar su funcionamiento local.
- Revisar la calidad, distribución y documentación del dataset.
- Explorar la integración entre el prototipo físico y la aplicación, sin asumir que ya existe.
- Diseñar y desarrollar la pantalla de retroalimentación inmediata.
- Investigar cómo se deben almacenar, transportar y entregar correctamente los materiales separados para evitar contaminación y asegurar su aprovechamiento.

## Próximas líneas de trabajo

### Inteligencia artificial y dataset
- Auditar las imágenes y anotaciones existentes.
- Revisar la distribución de las clases y los posibles errores de etiquetado.
- Evaluar el modelo con datos de prueba representativos.
- Investigar alternativas de optimización para Raspberry Pi 5.

### Hardware y mecanismo
- Reducir el tamaño y mejorar la transportabilidad del prototipo.
- Revisar la velocidad, precisión y confiabilidad del mecanismo.
- Evaluar la disposición de los compartimentos y el mantenimiento de la estación.

### Interacción y aprendizaje
- Investigar e implementar una pantalla física para ofrecer retroalimentación inmediata.
- Explorar mensajes educativos claros y adecuados para estudiantes.
- Evaluar cómo la interacción puede ayudar a comprender la separación correcta de materiales.

### Aplicación
- Continuar probando los conceptos de puntos y participación.
- Revisar la experiencia de usuario y la estructura de datos.
- Investigar posibles formas de conexión futura con el sistema físico.

### Validación
- Realizar pruebas controladas y, cuando sea posible, pruebas en entornos escolares.
- Documentar errores, limitaciones y oportunidades de mejora.
- Recoger observaciones de estudiantes, docentes y personas con experiencia en reciclaje y gestión de residuos.

## ¿Cómo colaborar?

Las contribuciones son bienvenidas. No es necesario ser programador ni tener experiencia técnica para aportar al proyecto.

Se puede colaborar en las siguientes áreas:

- **Inteligencia artificial y tecnología:** sugerencias sobre visión artificial, Python, YOLOv8, Raspberry Pi y optimización.
- **Dataset:** revisión de imágenes, anotaciones, categorías, calidad y organización de los datos.
- **Reciclaje y gestión de residuos:** comentarios y conocimientos sobre identificación y clasificación de materiales, contaminación cruzada, separación, almacenamiento, transporte, recolección y procesos de reciclaje.
- **Hardware y diseño:** observaciones sobre mecanismos, materiales, distribución de componentes, mantenimiento y facilidad de uso.
- **Educación y experiencia escolar:** ideas para explicar el reciclaje, mejorar la interacción con estudiantes y diseñar mensajes educativos.
- **Documentación y pruebas:** revisión de instrucciones, detección de errores y sugerencias para mejorar el proyecto.

Si tienes una observación o conocimiento que pueda ayudar, puedes abrir un *Issue* en el repositorio y describir tu propuesta. Las contribuciones serán revisadas por el equipo antes de incorporarse al proyecto.

Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para conocer las pautas de colaboración.

## Equipo

Proyecto desarrollado por:

- Sabrina Matos
- Rafic Saab
- Orbyteens

**BINNSIE by Orbyteens**

## Propiedad intelectual y uso del contenido

Este repositorio tiene como propósito documentar el desarrollo de BINNSIE, compartir información sobre el proyecto y facilitar la colaboración en aspectos seleccionados de su desarrollo. La licencia del repositorio y las condiciones de uso de sus distintos componentes están pendientes de definición. La publicación de este repositorio no debe interpretarse como una autorización general para comercializar, reproducir o reutilizar todos los elementos del proyecto. Antes de publicar código, imágenes, diseños o documentación, se revisarán los derechos de autor, las licencias de terceros y la información confidencial correspondiente.

## Estado del proyecto

**En desarrollo experimental y etapa de prototipado.**

BINNSIE continúa evolucionando mediante pruebas, aprendizaje y colaboración. La documentación se actualizará a medida que se validen nuevas funcionalidades y avances.

---

**BINNSIE by Orbyteens**  
*Tecnología, educación y sostenibilidad.*
