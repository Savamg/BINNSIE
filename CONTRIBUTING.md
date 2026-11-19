# Contributing to BINNSIE

Thank you for your interest in contributing to BINNSIE!

BINNSIE is an educational smart recycling ecosystem focused on schools. It brings together a physical recycling station, computer vision, a digital application, environmental education, and responsible recycling management.

**The bin sorts, the student learns.**

Contributions are welcome from people with different backgrounds. You do not need to be a programmer or engineer to share useful feedback, observations, or ideas.

## Project at a glance

BINNSIE is more than an application or a recycling bin. Its main areas are:

- **Physical engineering:** a recycling-station prototype with a structure, collection compartments, camera, and motorized mechanisms.
- **Artificial intelligence:** a YOLOv8s object-detection model currently trained for Metal, Paper, and Plastic.
- **Digital application:** an experimental web application prototype developed separately from the physical station.
- **Education and engagement:** an approach intended to help students understand recycling through interaction and learning.
- **Recycling management:** attention to collection and appropriate handling of recovered materials.

The AI model has undergone preliminary testing on Raspberry Pi 5. Recognition can vary with lighting and object orientation or positioning, and further testing is needed. The application is not yet integrated with the physical station. These are important distinctions when proposing or describing project improvements.

## Ways to contribute

### 1. Artificial intelligence and computer vision

We welcome suggestions related to material detection, model evaluation, and edge-device deployment.

Examples:
- Identify possible causes of missed detections or incorrect classifications.
- Suggest evaluation methods for object-detection models.
- Recommend approaches suitable for Raspberry Pi 5.
- Share relevant research or technical resources.
- Suggest ways to evaluate lighting, camera angle, and object orientation.

The current model classes are **Metal, Paper, and Plastic**. This does not mean every object in those material categories can already be detected reliably.

### 2. Dataset and image quality

Image diversity and consistent annotations are important to model development.

You can:
- Report possible annotation inconsistencies.
- Suggest ways to improve image quality or dataset balance.
- Identify challenging material appearances or visual conditions.
- Recommend image collection and review practices.
- Share references to image resources that may be legally used.

Do not upload the complete dataset, private annotations, model weights, training checkpoints, or restricted training resources. Do not share images unless you own the rights or have permission to share them. For suggestions, describe the issue or provide a permitted reference rather than publishing private dataset contents.

The team plans to collect additional images using the Raspberry Pi Camera. That collection and the subsequent retraining are future work, not completed milestones.

### 3. Hardware, electronics, and mechanical engineering

Possible contributions include:
- Suggestions for sorting mechanisms and mechanical reliability.
- Recommendations for motors, sensors, and electronic components.
- Ideas for structural improvements, maintenance, and accessibility.
- Feedback on Raspberry Pi and embedded-system approaches.
- Safety and durability considerations for school environments.

Do not publish private technical configurations, access details, or sensitive implementation files.

### 4. Recycling practices and material management

Practical knowledge about recycling is valuable, even without technical experience.

We welcome:
- Information about recyclable material identification.
- Suggestions for reducing cross-contamination.
- Recommendations for storage and handling.
- Information about collection centers, recycling facilities, and material managers.
- Evidence-based information about what happens to materials after collection.
- Suggestions for school recycling practices.

Please include sources when making technical, environmental, or regulatory claims.

### 5. Application and user experience

The application is an experimental prototype and currently operates separately from the physical station.

You can suggest:
- Improvements to navigation, accessibility, and usability.
- Educational features and recycling guidance.
- Ideas for points, achievements, and community participation.
- Improvements to QR-related interactions.
- Feedback on maps, station information, and reporting features.

A feature visible in the prototype should not automatically be assumed to be fully implemented, tested, or connected to the hardware.

### 6. Education, communication, and documentation

You can contribute by:
- Suggesting activities for students and schools.
- Recommending reliable educational resources.
- Reviewing documentation for clarity and consistency.
- Identifying outdated or unsupported claims.
- Suggesting ways to explain recycling concepts to children and adolescents.

### 7. Recycling partnerships and implementation

Suggestions about school pilots, collection logistics, recycling partners, and responsible downstream handling are welcome. Please distinguish confirmed arrangements from potential partners or recommendations.

## How to contribute

### Option 1: Open an Issue

Use an Issue to report a problem, propose an improvement, suggest a dataset review, or share recycling knowledge.

1. Visit the [Issues section](https://github.com/Savamg/BINNSIE/issues).
2. Check whether a similar Issue already exists.
3. Select the most relevant template.
4. Describe the observation or proposal clearly.
5. Include relevant sources or evidence when appropriate.
6. Submit the Issue for review.

You do not need programming experience to open an Issue. An Issue is a discussion and does not mean that a proposed change has been approved or will be implemented.

### Option 2: Submit a Pull Request

Pull Requests propose specific changes to files in this repository.

**Generally suitable for direct Pull Requests:**
- Documentation corrections and clarifications.
- Spelling, grammar, and formatting improvements.
- Improvements to educational text, provided claims are supported by reliable sources.
- Corrections to broken links or image references.

**Discuss first through an Issue:**
- Changes to the application's implementation.
- Changes to AI model architecture, training, or dataset structure.
- Hardware designs and mechanical or electronic implementations.
- Changes involving external services, integrations, or operational workflows.
- Any change that could expose private or sensitive project resources.

Please wait for maintainer feedback before starting work in areas that require prior discussion.

For an approved contribution:
1. Fork the repository.
2. Create a separate branch for your changes.
3. Make focused modifications.
4. Review the diff before submitting.
5. Check links, image paths, and Markdown rendering where relevant.
6. Submit a Pull Request with a clear explanation and any useful evidence.

A Pull Request may be revised or declined after review.

## Contribution and safety guidelines

- Explain the purpose and scope of your contribution.
- Search existing Issues before opening a new one.
- Be respectful, specific, and constructive.
- Provide sources for technical, scientific, environmental, or regulatory claims.
- Do not upload passwords, API keys, access tokens, database credentials, environment files, or other secrets.
- Do not publish personal, confidential, or identifying information.
- Do not upload private datasets, original annotation collections, model weights, checkpoints, or unpublished training configurations.
- Do not submit third-party content without the necessary rights or permissions.
- Avoid photographs that identify students or other people. Obtain appropriate permissions before collecting or sharing images from school environments.
- Do not attempt to access or modify external services, accounts, or infrastructure connected to the project.
- Do not present proposed features, planned tests, or potential partnerships as completed or confirmed.

If you discover a security or privacy issue, do not publish secrets or exploit details in a public Issue. Report the concern without including sensitive information and contact the project maintainers through an appropriate private channel if one is provided.

## Project status and review

BINNSIE is an evolving experimental project. Its components are at different stages: the physical station has been prototyped, the AI model has undergone preliminary Raspberry Pi 5 testing, the application remains an experimental separate prototype, and full system integration and school validation remain development goals.

Contributions are reviewed according to relevance, feasibility, safety, evidence, and consistency with the project's objectives. Public availability of this repository does not mean every internal component or implementation is open for modification.

## Intellectual property and submitted contributions

Before submitting material, make sure you have the right to share it. Do not submit confidential, proprietary, or restricted information belonging to another person or organization.

The licensing and reuse conditions for BINNSIE's different components have not yet been fully defined. Do not assume that public access to this repository grants permission to reproduce, distribute, or commercially use every part of the project.

If you are unsure whether material can be included, discuss it with the project maintainers before submitting it.

## Questions

For questions, suggestions, or proposed contributions, open an Issue in this repository.

Thank you for helping improve BINNSIE. Technical, educational, environmental, and practical contributions are all valuable.

**BINNSIE**

*The bin sorts, the student learns.*
