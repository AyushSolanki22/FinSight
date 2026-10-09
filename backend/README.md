# Backend services

This repository deliberately separates:
- `mern-api`: primary Node/Express API and MongoDB persistence
- `java-service`: optional Spring Boot service for a distinct Java responsibility
- `ai-service`: Python service lives at repository root in `ai-service/`

For the mini-project MVP, keep MERN as the main API gateway. Add Java only if the team can define a non-duplicated responsibility (for example, a separately deployed reporting/export service).
