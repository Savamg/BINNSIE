# BINNSIE Documentation

Welcome to the documentation section of **BINNSIE**, an educational smart recycling project focused on improving waste separation in schools through physical engineering, artificial intelligence, digital tools, and environmental education.

**The bin sorts, the student learns.**

This folder contains the project overview and supporting documents. Documentation for the application and machine learning component is maintained in their respective directories.

## Documentation available

| Resource | Description |
|---|---|
| [Project Overview](Project%20overview.md) | Explains BINNSIE's concept, design principles, school-focused approach, and long-term vision. |
| [Supporting Document 1](binnsie-Supporting%20doc1.pdf) | First supporting document submitted for The Earth Prize. |
| [Supporting Document 2](Binnsie-%20Supporting%20doc2.pdf) | Second supporting document submitted for The Earth Prize. |
| [Application Overview](../app/README.md) | Describes the experimental web application, its intended features, technologies, and current limitations. |
| [Machine Learning Overview](../ml/README.md) | Summarizes the current object-detection model, training results, limitations, and development workflow. |
| [Main Repository README](../README.md) | Project introduction, current development overview, prototype images, and repository scope. |

## Project areas

BINNSIE brings together five connected areas:

1. **Physical engineering:** a prototype recycling station with a structure, collection compartments, camera, and motorized mechanisms.
2. **Artificial intelligence:** a YOLOv8s object-detection model currently trained to identify three material classes: Metal, Paper, and Plastic.
3. **Digital application:** an experimental web application prototype developed with Lovable, React, TypeScript, Vite, and Supabase.
4. **Education and engagement:** educational content and participation features intended to make recycling more understandable and engaging for students.
5. **Recycling management:** attention to collection and appropriate downstream handling, recognizing that separation alone does not complete the recycling process.

These areas are at different stages of development and are not yet fully integrated into one operational system.

## Repository contents and scope

The public repository currently includes:

- Project documentation and the two supporting PDF documents.
- An overview of the experimental application; the application's full source code is not included here.
- Machine learning documentation, including the Model Card, Dataset Card, Training Methodology, and selected training and validation visualizations. The complete dataset, annotation files, and model weights are not included.
- Selected visual assets, including prototype photographs, the BINNSIE logo, mascot, and application screenshots.
- Contribution guidelines and GitHub issue templates.

The public repository intentionally does not publish every internal implementation file, dataset, model checkpoint, credential, or technical configuration. Its contents should not be interpreted as a complete build guide or as confirmation that every planned feature is operational.

## Development status

BINNSIE is an evolving experimental project. The physical station has been prototyped, the AI model has undergone preliminary testing on Raspberry Pi 5 and is being improved, and the application remains an experimental prototype developed separately from the physical hardware.

Descriptions of intended workflows and future features are not claims that those components are already integrated or fully validated. Further testing in school environments and collaboration with recycling partners are still important steps.

## Contributing

Suggestions, corrections, and constructive feedback are welcome. Please read the [Contributing Guidelines](../CONTRIBUTING.md) before proposing changes.

You can also report an issue or share a suggestion through the [GitHub Issues page](https://github.com/Savamg/BINNSIE/issues).

---

**BINNSIE**

*The bin sorts, the student learns.*
