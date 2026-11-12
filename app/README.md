# BINNSIE Application

The BINNSIE application is the digital component of the BINNSIE project. It is designed to complement the smart recycling station through tools for interaction, information, tracking, and community participation.

It is currently an experimental prototype developed with **Lovable**, using **React, TypeScript, Vite, and Supabase**.

## Purpose

The application aims to provide a platform that encourages users to participate in recycling activities, access information about recycling stations, and explore gamification features that support environmentally responsible habits.

## Functional Structure

- **Home and navigation:** landing pages and general navigation.

  <p align="center">
    <img src="../assets/orbyteens-landingPage.png" width="80%" alt="BINNSIE application landing page">
  </p>

- **Authentication and profiles:** registration, sign-in, password recovery, and user profiles.

- **Recycling and QR codes:** pages designed for QR code scanning and recycling-related interactions.

  <p align="center">
    <img src="../assets/orbyteens-scan.png" width="80%" alt="BINNSIE QR scanning screen">
  </p>

- **Maps and stations:** station visualization and information related to recycling containers.

  <p align="center">
    <img src="../assets/orbyteens-map.png" width="80%" alt="BINNSIE recycling station map">
  </p>

- **Community and reports:** tools for sharing information and reporting issues.

  <p align="center">
    <img src="../assets/orbyteens-reportIssues.png" width="80%" alt="BINNSIE community issue reporting screen">
  </p>

- **Environmental education:** educational content and recycling guidance. (Future implementation)

- **Gamification:** user profiles, points, achievements, and leaderboards.

  <p align="center">
    <img src="../assets/orbyteens-leaderboard.png" width="45%" alt="BINNSIE leaderboard">
    <img src="../assets/orbyteens-community.png" width="45%" alt="BINNSIE community screen">
  </p>

- **Administration and management:** dashboards and tools for different user roles.

## Technical Components

The application is organized around reusable components, pages, contexts, hooks, and integration modules.

These include navigation tools, route protection, language selection, QR code features, and achievement displays.

## Technologies

| Technology | Purpose |
|---|---|
| Lovable | AI-assisted application development. |
| React | User interface development. |
| TypeScript | Statically typed application development. |
| Vite | Development server and build tool. |
| Supabase | Backend services, authentication, and data management. |
| Tailwind CSS | Interface styling. |

## Relationship with the Physical Station

The application and the BINNSIE physical station are complementary components of the project.

The physical station focuses on identifying and sorting recyclable materials through computer vision and automated mechanisms.

The application focuses on user interaction, recycling information, community participation, and gamification.

**Important:** The current application prototype operates independently of the station's hardware. Direct integration between these components is a possibility for future development stages.

## Development Status

The application is in an experimental prototyping stage. Its architecture and features may evolve as the project progresses.

The presence of pages or components in the application does not necessarily mean that every feature is fully implemented, tested, or integrated.

## Future Development

Potential areas for future development include:

- Integration with the BINNSIE physical station.
- Data synchronization between the application and hardware.
- Improvements to the gamification system.
- Expansion of educational content.
- Further testing and improvements to the QR code system.
- Improvements in accessibility, security, and user experience.

---

Part of the BINNSIE project.

**The bin sorts, the student learns.**
