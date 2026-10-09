# FinSight
### Evidence-grounded, multi-agent financial research for Indian listed companies

FinSight is a project to explore how multi-agent AI can help research companies listed on the **National Stock Exchange of India (NSE)** and **BSE**. A user asks a natural-language question; the system is designed to gather financial data, retrieve evidence from company filings, run calculations with Python, verify key claims, and assemble an analyst-style report with traceable citations.

> **Project status:** Initial scaffold. The repository contains starter structure and service entry points; most agent workflows, data integrations, persistence, retrieval, and verification features still need to be implemented.

---

## Contents

- [Problem](#problem)
- [Goals](#goals)
- [Example query](#example-query)
- [How it works](#how-it-works)
- [Technology stack](#technology-stack)
- [Repository structure](#repository-structure)
- [Getting started](#getting-started)
- [Configuration](#configuration)
- [API endpoints](#api-endpoints)
- [Reliability principles](#reliability-principles)
- [Team workflow](#team-workflow)
- [Development roadmap](#development-roadmap)
- [Testing and evaluation](#testing-and-evaluation)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)


## Problem

Financial research often requires reading long filings, collecting data from multiple sources, calculating metrics consistently, and checking whether conclusions are supported by evidence. LLM-only answers can introduce unsupported claims or arithmetic mistakes.

FinSight is designed to address these problems by separating **retrieval, deterministic computation, interpretation, and verification** rather than asking one language model to do everything.

## Goals

- Research a focused set of Indian listed companies.
- Retrieve relevant evidence from annual reports and other company filings.
- Calculate financial and stock metrics in Python, not in an LLM response.
- Link factual claims to source documents and, where possible, page numbers.
- Distinguish sourced facts, calculated values, interpretations, and uncertainty.
- Evaluate numeric accuracy, citation quality, and retrieval performance.

## Example query

> “How have Reliance Industries’ debt and profit margins changed over the last five years, and what risks did management highlight?”

The intended report can include:
- A concise company and period overview
- Revenue, profit, debt, and margin trends
- Selected stock-performance metrics
- Risks explicitly disclosed by management
- Citations to supporting filings or datasets
- A verification summary and limitations

The example is illustrative. It does not imply that the current scaffold already retrieves or calculates these results.

## How it works

```text
React Frontend
      |
      v
MERN API (Express)
      |
      v
Python AI Service (FastAPI)
      |
      v
LangGraph Workflow
  |          |           |
  v          v           v
Data      Filing/RAG    Risk
Agent      Research     Agent
  |          |           |
  +----------+-----------+
             |
             v
     Python Quant Engine
             |
             v
       Verification
             |
             v
       Report Assembly
             |
             v
      Cited Research Report
```

### Main components

1. **Planner Agent** — converts a research question into structured tasks.
2. **Data Agent** — obtains and normalizes supported financial and market data.
3. **Filing Research Agent** — retrieves relevant filing passages through RAG.
4. **Risk Agent** — extracts management-disclosed risks with evidence.
5. **Quant Engine** — computes supported metrics deterministically in Python.
6. **Verification layer** — checks computed values and source metadata before publication.
7. **Report Agent** — assembles the results into a readable report.

The quant engine and validators should be ordinary, testable code wherever possible; they do not need to be autonomous LLM agents.

## Technology stack

| Layer | Technology | Responsibility |
|---|---|---|
| Frontend | React, Vite | Research UI, charts, report and citation views |
| Main application API | Node.js, Express | API gateway and application endpoints |
| Application database | MongoDB, Mongoose | Saved report metadata and future user/application data |
| Optional Java service | Java, Spring Boot, Maven | A separate, clearly bounded service if needed |
| AI API | Python, FastAPI | AI workflow entry point |
| Agent orchestration | LangGraph | Workflow and agent coordination |
| Retrieval | ChromaDB | Vector search over document chunks and metadata |
| Quantitative analysis | Python, Pandas, NumPy | Reproducible calculations |
| Deployment | Docker, Docker Compose | Local service orchestration |
| Observability | Langfuse (planned) | Tracing and evaluation support |

**Storage distinction:** ChromaDB is used for vector retrieval over unstructured filings. It is not a replacement for MongoDB or a structured financial database. Financial values should be stored in a consistent, validated structure with units, periods, and source information.

## Repository structure

```text
FinSight/
├── frontend/                    # React + Vite
│   └── src/
│       ├── app/                 # App shell and routes
│       ├── pages/               # Research, analysis, dashboard, reports
│       ├── components/          # Reusable UI components
│       ├── services/            # API client
│       └── styles/
├── backend/
│   ├── mern-api/                # Node.js + Express + MongoDB
│   │   └── src/
│   │       ├── routes/
│   │       ├── controllers/
│   │       ├── services/
│   │       ├── models/
│   │       ├── middleware/
│   │       └── database/
│   └── java-service/            # Optional Spring Boot service
├── ai-service/                  # Python + FastAPI
│   └── app/
│       ├── agents/
│       ├── workflows/
│       ├── rag/
│       ├── quant/
│       ├── verification/
│       ├── evaluation/
│       └── api/
├── data/
│   ├── raw/                     # Local source data; do not commit private/large files
│   ├── processed/
│   └── sample_data/
├── storage/
│   └── chroma/                  # Persistent local ChromaDB files
├── scripts/                     # Ingestion and import scripts
├── docs/                        # Architecture, API, evaluation notes
├── docker-compose.yml
└── README.md
```

## Getting started

### Prerequisites

Install the tools relevant to the services you plan to run:

- Git
- Node.js and npm
- Python 3.11+ (use a version compatible with the chosen dependencies)
- MongoDB locally or a MongoDB connection URI
- Java 21 and Maven only if you use `backend/java-service`
- Docker Desktop / Docker Engine if using containers

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd FinSight
```

Replace `<your-repository-url>` with your team's Git repository URL.

### 2. Start the React frontend

```bash
cd frontend
npm install
```

Copy `.env.example` to `.env` if needed, then start the development server:

```bash
npm run dev
```

Vite normally serves the frontend at `http://localhost:5173`.

### 3. Start the MERN API

In a separate terminal:

```bash
cd backend/mern-api
npm install
```

Copy `.env.example` to `.env`, set `MONGODB_URI`, and start MongoDB. Then run:

```bash
npm run dev
```

The API is configured for `http://localhost:5000`. The current health route is:

```text
GET http://localhost:5000/api/v1/health
```

### 4. Start the Python AI service

In a separate terminal:

```bash
cd ai-service
python -m venv .venv
```

Activate the environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

Install dependencies and start the API:

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env`, then run:

```bash
uvicorn app.main:app --reload --port 8000
```

Health check:

```text
GET http://localhost:8000/api/v1/health
```

The analysis endpoint is currently a scaffold and returns a placeholder response until the workflow is implemented.

### 5. Run the Java service (optional)

Use Java 21 and Maven:

```bash
cd backend/java-service
mvn spring-boot:run
```

Health check:

```text
GET http://localhost:8080/api/v1/health
```

Only add this service to the active architecture if the team assigns it a specific responsibility that is not already handled by the MERN API or Python AI service.

### Docker note

A starter `docker-compose.yml` is included, but container orchestration should be treated as a template and may need adjustment as service implementations evolve. Create local `.env` files from the examples before starting the services. Do not put real API keys in source control.

## Configuration

Configuration examples are provided at the root and within each service.

| Variable | Used by | Purpose |
|---|---|---|
| `VITE_API_BASE_URL` | React | Base URL for the MERN API |
| `PORT` | MERN API | Express server port |
| `MONGODB_URI` | MERN API | MongoDB connection URI |
| `FRONTEND_URL` | MERN API | Allowed frontend origin for CORS |
| `AI_SERVICE_URL` | MERN API | Python AI service base URL |
| `CHROMA_PERSIST_DIRECTORY` | AI service | ChromaDB persistence directory |
| `CHROMA_COLLECTION_NAME` | AI service | Filing collection name |
| `LLM_PROVIDER` | AI service | Selected model provider (planned) |
| `LLM_API_KEY` | AI service | Model API key, if required |
| `LLM_MODEL` | AI service | Model identifier, if required |

Variable names and behavior may evolve during implementation. Never commit `.env` files, access tokens, or secrets.

## API endpoints

These are the initial scaffold endpoints, not a promise that all features are complete.

### MERN API

| Method | Endpoint | Status |
|---|---|---|
| `GET` | `/api/v1/health` | Implemented health response |
| `POST` | `/api/v1/analysis` | Route exists; requires AI service integration |
| `GET` | `/api/v1/reports` | Placeholder |
| `GET` | `/api/v1/reports/:reportId` | Placeholder |

### Python AI service

| Method | Endpoint | Status |
|---|---|---|
| `GET` | `/api/v1/health` | Implemented health response |
| `POST` | `/api/v1/analysis` | Placeholder response; workflow pending |

### Java service

| Method | Endpoint | Status |
|---|---|---|
| `GET` | `/api/v1/health` | Implemented health response |

## Reliability principles

FinSight should follow these rules as features are implemented:

- **Code computes numbers.** The LLM must not be the authority for arithmetic.
- **Preserve provenance.** Store the source URL, document title, fiscal period, page number where available, retrieval date, unit, and relevant excerpt.
- **Validate units and periods.** Do not compare figures with mismatched currencies, scales, fiscal periods, or consolidated/standalone bases.
- **Distinguish claim types.**
  - `Directly sourced`: explicitly stated in a source.
  - `Calculated`: produced by a documented formula from known inputs.
  - `Inferred`: an interpretation derived from evidence.
  - `Uncertain`: evidence or data is insufficient.
- **Fail visibly.** If a metric cannot be calculated or a citation cannot be validated, label it as unavailable/uncertain instead of fabricating a value.
- **Keep research separate from advice.** Do not generate personalized buy/sell recommendations.

## Team workflow

A possible split for a team of 4–5:

- **Frontend:** React pages, charts, report display, citation viewer, API integration.
- **MERN backend:** Express endpoints, MongoDB models, saved reports, request validation.
- **AI/RAG:** PDF ingestion, chunking, embeddings, ChromaDB retrieval, citation metadata.
- **Quant/verification:** deterministic formulas, input validation, number checks, evaluation dataset.
- **Integration/Java/DevOps:** service contracts, Docker, tests, documentation, and a clearly scoped Java service if required.

Agree on API request/response schemas early. Keep work in feature branches and review changes through pull requests. Avoid having two services implement the same feature.

## Development roadmap

### Phase 1 — Working vertical slice
- Submit a company question from React.
- Route it through Express to FastAPI.
- Return a structured placeholder/report response.
- Display status and errors in the UI.

### Phase 2 — Data and quantitative metrics
- Choose a small, fixed set of companies.
- Import validated sample financial data.
- Implement and unit-test CAGR, margins, debt change, returns, volatility, and drawdown where data is available.
- Track source, units, and fiscal periods.

### Phase 3 — Filing RAG
- Ingest a limited set of annual reports.
- Preserve page-level metadata.
- Store chunks and embeddings in ChromaDB.
- Return relevant excerpts with citations.

### Phase 4 — Agents and verification
- Build the LangGraph workflow.
- Extract management-disclosed risks.
- Validate calculations and citations.
- Generate reports with claim labels and an explicit limitations section.

### Phase 5 — Evaluation and demo readiness
- Create a small gold-standard question set.
- Measure numeric accuracy, citation correctness, retrieval relevance, and verification performance.
- Add integration tests, Docker setup, and a documented demo flow.

## Testing and evaluation

At minimum, the team should test:

- Financial formulas against hand-checked expected results.
- Missing values, zero denominators, negative values, and mismatched units.
- Whether retrieval returns the correct filing and page.
- Whether citations actually support the associated claim.
- Whether verification catches deliberately incorrect numbers.
- API validation, error handling, and service-unavailable cases.

Do not claim a specific accuracy percentage until it has been measured on a documented test set.

## Contributing

1. Create an issue describing the change.
2. Create a feature branch, for example `feat/chroma-ingestion` or `feat/report-viewer`.
3. Keep changes scoped to the service you own.
4. Add or update tests and documentation.
5. Open a pull request and request a teammate review.
6. Never commit secrets, private credentials, or large/generated ChromaDB storage files.

## Disclaimer

FinSight is an educational and research project. It is not investment, legal, tax, or financial advice and must not be treated as a recommendation to buy, sell, or hold any security. Financial data can be incomplete, delayed, restated, or incorrectly interpreted. Users should independently verify source documents and consult qualified professionals before making financial decisions.
