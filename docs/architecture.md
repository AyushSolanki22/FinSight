# Architecture notes

## Service boundaries
- React: presentation only.
- MERN API: public API gateway, report metadata, user-facing application concerns.
- Python AI service: LangGraph workflow, RAG, numerical computation, verification.
- Java service: optional, only for a distinct responsibility.
- ChromaDB: vector retrieval for unstructured filings; not a substitute for structured financial storage.

## Trust boundaries
- Treat LLM output and retrieved document text as untrusted data.
- Every financial metric should record input values, formula/version, period, unit, and result.
- Every factual claim should carry source metadata or be explicitly marked as an inference/uncertain.
