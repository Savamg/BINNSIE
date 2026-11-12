# BINNSIE – Machine Learning

## Overview

BINNSIE's Machine Learning (ML) component uses computer vision to support the automatic identification and classification of recyclable materials.

The goal is to reduce the need for students to manually decide where each item belongs. Instead, the system is designed to identify materials and support the physical sorting process, making recycling more accessible while creating an educational experience.

**BINNSIE's guiding principle:**

> The bin sorts, the student learns.

This directory documents the machine learning component, its development, evaluation, current limitations, and planned deployment.

## Project Objectives

The ML system is being developed to:

- Detect recyclable materials using computer vision.
- Classify detected objects into material categories.
- Support the automated sorting mechanism of the BINNSIE station.
- Reduce incorrect material disposal and cross-contamination.
- Enable future offline inference on a Raspberry Pi 5.
- Support an educational recycling experience in schools.

## Current Detection Classes

The current model was trained to recognize three categories:

| Class | Description |
|---|---|
| Metal | Objects made primarily of metal |
| Paper | Paper-based recyclable materials |
| Plastic | Plastic recyclable materials |

These categories represent the current scope of the trained model. They do not imply that every object within each material category can already be detected reliably.

## Model Information

| Property | Current implementation |
|---|---|
| Task | Object detection |
| Architecture | YOLOv8s |
| Framework | Ultralytics |
| Training environment | Google Colab |
| Training hardware | NVIDIA Tesla T4 GPU |
| Dataset size | 4,001 images |
| Number of classes | 3 |
| Target deployment hardware | Raspberry Pi 5 |

The model was trained using a pretrained YOLOv8s checkpoint and fine-tuned with the BINNSIE dataset.

## Training and Evaluation

The latest documented training run used Ultralytics 8.4.38.

Training stopped after 91 epochs through early stopping. The best checkpoint was identified at epoch 71.

The validation results were:

| Class | Precision | Recall | mAP50 |
|---|---:|---:|---:|
| Metal | 0.778 | 0.688 | 0.755 |
| Paper | 0.823 | 0.806 | 0.808 |
| Plastic | 0.813 | 0.675 | 0.743 |
| **Overall** | **0.804** | **0.723** | **0.769** |

**Overall mAP50-95: 0.510**

The validation set contained 369 images and 820 annotated instances.

## Development Workflow

The machine learning development process includes the following stages:

1. **Data collection:** Gathering images of recyclable materials.
2. **Data preparation:** Organizing images and defining material categories.
3. **Annotation:** Labeling objects for supervised training.
4. **Model training:** Training and fine-tuning the object detection model.
5. **Evaluation:** Measuring precision, recall, and mean Average Precision (mAP).
6. **Optimization:** Exploring improvements for efficient inference on edge hardware.
7. **Deployment testing:** Evaluating the model on the intended Raspberry Pi 5 hardware.

## Hardware Integration

The intended deployment platform for BINNSIE's ML system is the Raspberry Pi 5.

The planned workflow is:

1. A camera captures an image of an item deposited into the station.
2. The ML model analyzes the image.
3. The system identifies the detected material category.
4. The classification result supports the physical sorting mechanism.

## Current Limitations

The ML component is still under development.

Current limitations and areas for improvement include:

- Improving detection performance, particularly for Metal and Plastic.
- Evaluating performance under different lighting conditions.
- Testing different object shapes, sizes, colors, and packaging conditions.
- Reducing incorrect classifications and missed detections.
- Evaluating inference speed and resource consumption on Raspberry Pi 5.
- Validating performance in the physical recycling station.

Further testing is necessary before the model can be considered ready for operational use.

## Privacy and Repository Policy

This repository documents the ML development process without exposing sensitive or unpublished project resources.

The following materials are not included in this public directory:

- Complete training datasets.
- Original annotation files.
- Model weights and checkpoints.
- Private training configurations.
- Credentials, API keys, or environment variables.

This approach allows contributors and interested readers to understand the technical direction of BINNSIE while protecting project resources.

## Future Development

Planned improvements include:

- Improving the quality and diversity of training data.
- Increasing detection performance across all three classes.
- Evaluating model optimization for edge devices.
- Testing offline inference on Raspberry Pi 5.
- Integrating the detection pipeline with the physical sorting mechanism.
- Validating the complete system in a school environment.

## About BINNSIE

BINNSIE is an educational smart recycling ecosystem designed for schools in Panama. It combines a physical intelligent recycling station, computer vision, a digital application, and student engagement to encourage better recycling practices.

The ML component is one part of this broader system.

For more information, visit the [main BINNSIE repository](https://github.com/Savamg/BINNSIE).
