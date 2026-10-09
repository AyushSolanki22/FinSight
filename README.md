# FinSight

Multi-agent AI financial research for Indian listed companies (NSE/BSE).

## Architecture
- `frontend/`: React + Vite user interface
- `backend/mern-api/`: Node.js + Express + MongoDB API (primary API gateway, users, saved reports)
- `backend/java-service/`: Java + Spring Boot service (optional domain/business service)
- `ai-service/`: Python + FastAPI, LangGraph, RAG, quant calculations, verification
- `storage/chroma/`: local persistent ChromaDB data (do not commit generated database files)
- `data/`: sample financial data and source filings

## Important design rules
1. Python is the source of truth for numerical calculations.
2. ChromaDB stores document chunks, embeddings, and source metadata; it is not the main store for financial tables or user accounts.
3. React talks to the MERN API. The MERN API calls the AI service and, when needed, the Java service.
4. The Java service is optional in the MVP. Avoid implementing the same business logic in both Node and Java.
5. Every generated report should preserve source URLs, document names, page numbers, and verification status.

## Suggested development order
1. Build the React UI and MERN API health endpoint.
2. Add MongoDB models for users and saved reports.
3. Build the Python AI service health endpoint and deterministic quant functions.
4. Add filing ingestion and ChromaDB retrieval.
5. Connect the MERN API to the AI service.
6. Add the Java service only for a clearly defined responsibility.
7. Add verification, evaluation tests, and Docker deployment.

## Local setup
Each service has its own README and `.env.example`. Copy environment examples to local `.env` files and supply your own values. Never commit secrets or API keys.
