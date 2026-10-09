# FinSight AI Service

Python + FastAPI service for LangGraph orchestration, RAG with ChromaDB, deterministic quantitative analysis, and output verification.

Run: create a virtual environment, install `requirements.txt`, copy `.env.example` to `.env`, then run:
`uvicorn app.main:app --reload --port 8000`

Keep numeric formulas in `app/quant/`. Treat model outputs as untrusted until validated.
