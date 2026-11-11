# BINNSIE
### The bin sorts, the student learns.

<p align="center">
  <em>An educational smart recycling ecosystem combining engineering, artificial intelligence, and environmental education.</em>
</p>

---

## About BINNSIE

BINNSIE is an educational smart recycling project developed to improve waste separation at the source and encourage sustainable habits in schools.

The project addresses a challenge that goes beyond the disposal of waste: recyclable materials are often mixed, contaminated, or incorrectly classified, making their recovery more difficult.

BINNSIE explores how technology can make recycling easier and more engaging by combining an intelligent physical recycling station, computer vision, digital tools, and student participation.

**BINNSIE is more than a recycling bin or an application. It is an ecosystem designed to connect waste separation with education.**

## The Problem

Improper waste management remains an important environmental challenge in Panama.

Limited source separation, contamination of recyclable materials, and difficulties in establishing consistent recycling habits all contribute to the problem.

Recycling requires more than asking people to separate their waste. It also requires accessible systems, clear guidance, appropriate infrastructure, and reliable material management.

BINNSIE aims to address these challenges through an educational and technology-based approach.

## Our Approach

BINNSIE combines five main areas:

### 1. Physical Engineering

An intelligent recycling station designed to receive waste and direct materials into designated compartments through a mechanical sorting system.

The physical prototype incorporates a structural frame, collection compartments, a camera, and motorized mechanisms.

### 2. Artificial Intelligence

A computer-vision system designed to identify recyclable materials and support automatic classification.

The current model works with three material classes:

- Metal
- Paper
- Plastic

The AI development process includes image collection, dataset preparation, model training, and performance evaluation.

### 3. Digital Application

A web application prototype developed with Lovable and Supabase.

It explores features such as:

- User profiles and recycling activity.
- Points and achievements.
- Community participation and rankings.
- Recycling location maps.
- Reports about recycling locations.
- Educational information.
- Administrative and organizational tools.

The application is currently developed separately from the physical hardware prototype.

### 4. Education and Engagement

BINNSIE aims to make recycling an interactive learning experience.

Through gamification, educational content, and immediate feedback, the project encourages students to understand the importance of proper waste separation and develop more sustainable habits.

A physical feedback display is also part of the project's future development plans.

### 5. Recycling Management

Proper separation is only one step in the recycling process.

BINNSIE recognizes the importance of collection, transportation, and appropriate treatment of recovered materials. Collaboration with recycling centers and material-management partners is an important area for further development.

## How It Works

The intended system workflow is:

1. A user places a recyclable item into the station.
2. A camera captures an image of the item.
3. The computer-vision model analyzes and classifies the material.
4. The classification guides the mechanical sorting mechanism.
5. The item is directed toward its designated compartment.
6. Digital and educational tools can support user participation and engagement.

The complete workflow is an ongoing development objective. Not every component is currently integrated into a single operational system.

## Technology

The project has explored and used technologies across different areas:

| Area | Technologies |
|---|---|
| Hardware | Raspberry Pi 5, camera, servo motors, sensors |
| Artificial Intelligence | Python, Ultralytics, YOLO, Roboflow |
| Model Training | Google Colab |
| Digital Application | Lovable |
| Backend and Database | Supabase |
| Physical Design | Mechanical construction and prototyping |

This list describes technologies used or explored during development. It does not imply that every component is part of a finalized deployment.

## Development Status

BINNSIE is an evolving project. Its components are at different stages of development.

| Component | Current status |
|---|---|
| Physical recycling station | Prototype built and tested |
| Mechanical sorting | Implemented in the prototype; undergoing refinement |
| Artificial intelligence | Trained model undergoing improvement |
| Digital application | Experimental web application prototype |
| Educational experience | Under development |
| Physical feedback display | Future development |
| Recycling partnerships | Further development and validation needed |

Further testing in real school environments is necessary to evaluate the system's reliability, usability, and educational impact.

## Project Vision

Our vision is to develop a replicable educational recycling system that helps schools improve waste separation while encouraging students to participate actively in environmental solutions.

We believe that technology can support better recycling practices when it is combined with education, accessible infrastructure, and responsible material management.

## Collaboration

We welcome constructive feedback, technical suggestions, and contributions that can help improve BINNSIE.

Areas of interest include:

- Mechanical and hardware engineering.
- Artificial intelligence and computer vision.
- Embedded systems and programming.
- Educational technology and user experience.
- Recycling practices and material management.
- Testing and technical documentation.

Please open an issue to suggest an improvement, report a problem, or discuss a potential contribution.

## Repository Scope

This public repository presents BINNSIE's concept, development, documentation, and selected project materials.

Not all internal implementation files, software components, datasets, or technical configurations are included.

Please review the repository documentation before proposing contributions.

---

<p align="center">
  <strong>BINNSIE</strong><br>
  <em>The bin sorts, the student learns.</em>
</p>
