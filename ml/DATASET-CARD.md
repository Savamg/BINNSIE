# BINNSIE AI Dataset Card

## 1. Dataset Overview

**Project:** BINNSIE  
**Purpose:** Recyclable material object detection  
**Total images:** 4,001  
**Original annotation categories:** 4  
**Associated project:** BINNSIE AI

The BINNSIE dataset was assembled to support the development of an object detection system capable of identifying recyclable materials.

It provides visual examples that help the model learn to distinguish between the material categories used by the BINNSIE intelligent recycling station.

## 2. Dataset Categories

The original dataset contains four annotation categories:

| Category | Description |
|---|---|
| Metal | Objects classified as metal |
| Paper | Objects classified as paper |
| Plastic | Objects classified as plastic |
| None | Additional category used for images without annotated recyclable objects |

The three intended recyclable material categories are Metal, Paper, and Plastic.

`None` does not represent a recyclable material. It was originally included as an additional annotation category for images without annotated recyclable objects.

## 3. Dataset Organization and Annotation

The dataset is structured for object detection training.

Images are annotated to identify the location and category of recyclable objects within each image.

The annotations provide the information required for the model to learn which objects belong to each material category.

Images without recyclable objects can also be used as negative examples in object detection training. These should be represented appropriately within the dataset format rather than as a separate material class.

Detailed annotation files and original dataset resources are not included in the public repository.

## 4. Dataset Limitations and Revision Decisions

During development, the team tested the use of the `None` category and identified classification confusion associated with its inclusion.

In particular, the model showed confusion when encountering objects outside its intended material categories.

Based on these observations, the team decided to remove `None` from a future dataset revision.

The next dataset version will focus on three intended material categories:

- Metal
- Paper
- Plastic

Images without recyclable objects may still be retained as negative examples, using the appropriate annotation format.

The revised dataset will be evaluated through a new training process before its adoption.

## 5. Planned Data Collection

The team plans to capture additional images directly using the Raspberry Pi Camera (Pi Camera).

The objective is to collect examples that better represent the visual conditions encountered by the BINNSIE recycling station.

The planned collection may include:

- Different recyclable object shapes and sizes.
- Different object orientations.
- Different camera viewing angles and distances.
- Various backgrounds.
- Different lighting conditions.
- Objects with different appearances and physical conditions.

Particular attention will be given to examples that have previously caused annotation or classification difficulties.

New images will need to be reviewed, classified, and annotated before being considered for future training.

This collection process has not yet been completed.

## 6. Data Quality and Future Improvements

Future dataset improvements will focus on:

1. Removing the problematic `None` category.
2. Reviewing the existing annotations.
3. Improving the diversity of visual examples.
4. Collecting images using the Raspberry Pi Camera.
5. Including challenging examples from real operating conditions.
6. Reviewing class representation and dataset balance.
7. Maintaining consistent annotation criteria across categories.

These improvements aim to provide more representative training data for future BINNSIE AI versions.

## 7. Privacy and Data Protection

BINNSIE is designed for educational environments, particularly schools.

Future image collection should focus on recyclable materials rather than people.

The team intends to avoid unnecessary capture or storage of identifiable student images and to consider appropriate school permissions and privacy safeguards.

The public repository does not include:

- The complete original dataset.
- Private annotated image collections.
- Restricted training resources.
- Sensitive data or credentials.

## 8. Dataset Access and Documentation

This document describes the dataset's purpose, categories, limitations, and planned improvements.

The original dataset and private annotation resources are not distributed through the public repository.

The documentation is intended to provide transparency about the data used in BINNSIE AI development without exposing restricted project resources.

---

*This document reflects the dataset's current development status and the team's planned improvements. Future dataset versions may differ in composition, annotation structure, and collection procedures.*
