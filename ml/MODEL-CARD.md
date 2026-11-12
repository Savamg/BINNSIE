# BINNSIE AI Model Card

## 1. Model Overview

**Project:** BINNSIE  
**Model:** YOLOv8s  
**Version:** BINNSIE AI v1  
**Task:** Object Detection  
**Framework:** Ultralytics  
**Target Platform:** Raspberry Pi 5  
**Training Environment:** Google Colab

BINNSIE AI is an object detection model developed to identify recyclable materials and support the automated sorting process of the BINNSIE intelligent recycling station.

The model is designed to recognize three material categories:

- **Metal**
- **Paper**
- **Plastic**

Its purpose is to support more accurate recycling at the source, reduce incorrect material disposal, and contribute to a more educational and accessible recycling experience in schools.

The AI model is one component of the broader BINNSIE ecosystem, which combines intelligent hardware, digital engagement, education, and responsible material management.

## 2. Intended Use

The model is intended to support:

- Automated identification of recyclable materials.
- Intelligent material sorting within the BINNSIE recycling station.
- Educational demonstrations about recycling and waste separation.
- Future improvements to automated waste classification.
- Local inference on embedded hardware.

The model is intended for controlled recycling environments, particularly schools.

It is not designed to identify people, determine the value of recyclable materials, or classify every possible type of waste.

## 3. Model and Training Information

| Attribute | Description |
|---|---|
| Model architecture | YOLOv8s |
| Detection task | Object Detection |
| Framework | Ultralytics |
| Dataset size | 4,001 images |
| Number of classes | 3 |
| Classes | Metal, Paper, Plastic |
| Training environment | Google Colab |
| Training hardware | NVIDIA Tesla T4 GPU |
| Training duration | 91 epochs |
| Best checkpoint | Epoch 71 |
| Intended edge device | Raspberry Pi 5 |

The model was trained using a dataset containing 4,001 images.

The initial training target was 130 epochs. However, training stopped after 91 epochs because of the early-stopping mechanism configured for the experiment. The best checkpoint was obtained at epoch 71.

## 4. Evaluation Results

The model was evaluated using a validation dataset containing 369 images and 820 annotated instances.

### Overall performance

| Metric | Result |
|---|---:|
| Precision | 0.804 |
| Recall | 0.723 |
| mAP@50 | 0.769 |
| mAP@50–95 | 0.510 |

### Performance by class

| Class | Precision | Recall | mAP@50 |
|---|---:|---:|---:|
| Metal | 0.778 | 0.688 | 0.755 |
| Paper | 0.823 | 0.806 | 0.808 |
| Plastic | 0.813 | 0.675 | 0.743 |

These results represent validation performance during model development.

They should not be interpreted as guaranteed real-world sorting accuracy or as a measurement of the complete BINNSIE station.

## 5. Raspberry Pi 5 Testing

The BINNSIE AI model has already been tested on a Raspberry Pi 5.

Preliminary testing demonstrated that the model can detect recyclable objects on the target hardware. However, its recognition performance varies depending on environmental conditions and object positioning.

The following observations were identified:

### Lighting conditions

The model's ability to recognize objects depends on lighting conditions. Under certain lighting conditions, it may fail to detect or correctly recognize an object.

### Object orientation

The orientation and positioning of an object can affect recognition. The model occasionally confuses material categories when objects are presented at different angles or positions.

### Classification consistency

Some objects are incorrectly classified, demonstrating that further training and testing are necessary to improve recognition consistency.

These observations come from preliminary hardware testing. They are not the results of a controlled performance benchmark.

## 6. Known Limitations

Current limitations include:

- Detection performance varies with lighting conditions.
- Object orientation and camera viewing angles can affect recognition.
- Some objects may be assigned to the wrong material category.
- The model currently recognizes only three material categories.
- Different shapes, textures, backgrounds, and object conditions may affect detection.
- Validation metrics do not guarantee equivalent performance in real-world recycling conditions.
- Further testing is required to establish reliability during continuous operation.

These limitations are important considerations for future development and deployment.

## 7. Planned Dataset Improvement

One of the planned improvements is to capture additional images directly using the Raspberry Pi Camera (Pi Camera).

The objective is to collect images under conditions that more closely represent the actual environment in which BINNSIE operates.

Potential image variations include:

- Different lighting conditions.
- Different object orientations and viewing angles.
- Different distances from the camera.
- Various backgrounds and environments.
- Different shapes, sizes, and appearances of recyclable materials.
- Objects that the current model fails to recognize or incorrectly classifies.

The captured images can be reviewed, labeled, and incorporated into future training iterations.

This approach may help reduce the difference between the original training dataset and the images encountered during actual operation.

**Important:** This is a planned improvement. The new image collection and subsequent retraining should not be considered completed until they have been carried out and evaluated.

## 8. Deployment and Hardware Integration

The Raspberry Pi 5 is the intended edge-computing platform for BINNSIE.

The objective is to perform material detection locally, reducing dependence on a continuous internet connection.

The model has already undergone preliminary testing on Raspberry Pi 5. However, additional optimization and testing are needed to improve recognition under different lighting and object-positioning conditions.

Future hardware development aims to connect the detection system with the physical sorting mechanism, allowing identified materials to be directed into their corresponding containers.

The reliability of the complete sorting process has not yet been established through controlled system-level testing.

## 9. Responsible Use and Privacy

BINNSIE is designed as an educational recycling system.

Its computer vision functionality focuses on identifying recyclable materials rather than identifying people.

Future image collection should prioritize recyclable objects and avoid unnecessary capture of students or other identifiable individuals.

Appropriate school permissions, image-handling procedures, and privacy safeguards should be considered before collecting or using images in educational environments.

The public repository does not include:

- Private datasets or original annotated image collections.
- Trained model weights.
- Credentials, API keys, or passwords.
- Sensitive implementation details.
- Private configuration files.

## 10. Future Development

Future development priorities include:

1. Capturing additional training images using the Raspberry Pi Camera.
2. Improving recognition under different lighting conditions.
3. Increasing robustness to object orientation and viewing angles.
4. Reviewing and labeling difficult detection examples.
5. Retraining and evaluating future model versions.
6. Measuring inference speed and resource usage on Raspberry Pi 5.
7. Improving classification consistency across all three material categories.
8. Integrating the detection system with the physical sorting mechanism.
9. Conducting controlled tests to measure sorting accuracy and material contamination.

## 11. Project Context

BINNSIE aims to make recycling more accessible, understandable, and engaging in schools.

The AI model is one part of a broader ecosystem that combines intelligent recycling hardware, a digital application, educational activities, and gamification.

By identifying materials automatically, BINNSIE aims to reduce the burden of manual sorting while helping students understand how recycling works.

**The bin sorts, the student learns.**

---

*Documentation reflects the development and testing status of BINNSIE AI at the time of publication. Model performance, hardware integration, and future improvements may change as development progresses.*
