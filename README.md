# FinSight

FinSight is a financial research assistant prototype for exploring Indian listed companies. Users can ask questions through a chat-style interface, and the backend runs a research workflow to produce a written report.

> **Project status:** FinSight is an evolving prototype. The availability and quality of analysis depend on the data, integrations, and API credentials configured for the project. Verify important figures against official sources.

## Contents

- [The problem](#the-problem)
- [Project goals](#project-goals)
- [Features](#features)
- [Example query](#example-query)
- [How it works](#how-it-works)
- [Technology stack](#technology-stack)
- [Repository structure](#repository-structure)
- [Getting started](#getting-started)
- [Configuration](#configuration)
- [API endpoints](#api-endpoints)
- [Frontend commands](#frontend-commands)
- [Team](#team)
- [Responsible use](#responsible-use)

## The problem

Financial information about a company can be spread across filings, market data, and reports. Finding relevant information, comparing it, and turning it into a useful summary can take time. FinSight aims to make that research process easier by giving users one place to ask company-related questions and receive a structured response.

## Project goals

- Make company research easier to start with natural-language questions.
- Connect research questions to available company and market data.
- Calculate useful metrics from available financial information.
- Present findings in a clear report through a simple web interface.
- Make the research workflow and its limitations understandable to users.

## Features

- React frontend built with Vite.
- Home, Analysis, Features, Help, and About sections.
- Bright and dark appearance modes.
- Chat-style interface for submitting financial research questions.
- FastAPI endpoints for health checks and analysis requests.
- LangGraph-based research workflow.
- Quantitative analysis of available financial statements and market data.
- Backend support for selected Indian tickers: `RELIANCE`, `TCS`, `INFY`, `HDFCBANK`, and `ICICIBANK`.

Demo company cards and prices should be treated as illustrative unless the application identifies them as live data.

## Example query

```text
Summarize the available financial information about Reliance Industries.
Include revenue, profitability, debt, and any notable risks in the data.
```

A ticker can also be supplied with an API request, for example `RELIANCE`.

## How it works

1. The user submits a financial research question in the frontend.
2. The frontend sends the question to the FastAPI analysis endpoint.
3. The backend validates the request and supported ticker, if provided.
4. The research workflow plans the analysis and gathers available evidence and data.
5. Quantitative steps calculate metrics from the data that is available.
6. The backend returns a written report to the frontend.

The exact sources and calculations available depend on the project configuration and retrieved data. The prototype should not be assumed to provide complete coverage for every company or question.

## Technology stack

| Area | Technologies |
|---|---|
| Frontend | React, Vite, React Router, Axios, Recharts, Lucide React |
| Backend API | Python, FastAPI, Pydantic |
| Research workflow | LangGraph |
| AI providers | Groq, Google Gemini |
| Data and storage | Yahoo Finance, ChromaDB, SQLite |

## Repository structure

```text
FinSight/
├── backend/
│   └── app/
│       ├── agents/       # Research workflow and agents
│       ├── quant/        # Financial calculations
│       ├── tools/        # Market data and agent tools
│       └── main.py       # FastAPI application and API routes
├── frontend/
│   └── src/
│       ├── app/          # Application layout and shared state
│       ├── pages/        # Home, Analysis, Features, Help, About
│       ├── services/     # Frontend API integration
│       └── styles/       # Application styles
├── data/                 # Project data
├── docs/                 # Documentation
├── scripts/              # Utility scripts
├── storage/              # Local database and vector-store data
├── requirements.txt      # Python dependencies
└── docker-compose.yml    # Docker configuration
```

## Getting started

### Requirements

- Python 3.10 or later
- Node.js and npm
- API credentials for the providers used by the backend workflow

### 1. Open the repository root

Run the backend commands from the project root—the directory containing `requirements.txt` and the `backend` folder.

```bat
cd /d C:\Users\acer\GitHub\FinSight
```

### 2. Create and activate a Python virtual environment

```bat
python -m venv .venv
.venv\Scripts\activate
```

If `python` is not recognized, install Python, enable **Add Python to PATH**, and open a new terminal.

### 3. Install backend dependencies

```bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Start the backend

With the virtual environment active and the terminal at the repository root:

```bat
python -m uvicorn backend.app.main:app --reload --reload-dir backend
```

The API should be available at <http://127.0.0.1:8000>. Leave this terminal running.

### 5. Install and start the frontend

Open a second terminal:

```bat
cd /d C:\Users\acer\GitHub\FinSight\frontend
npm install
npm run dev
```

Open the URL printed by Vite, usually <http://localhost:5173>. Keep both terminals running while using the application.

## Configuration

Create a `.env` file in the repository root. Use `.env.example` as a template if it exists. The backend workflow discussed for this project requires credentials such as:

```dotenv
GROQ_API_KEY=your_groq_api_key
GEMINI_API_KEY=your_google_gemini_api_key
```

Keep real keys private. Do not place them in frontend files or commit them to Git. Check that `.env` is excluded by `.gitignore` before committing.

After changing `.env`, restart the backend so it loads the updated configuration.

## API endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Confirms that the API is running |
| `GET` | `/api/v1/health` | Returns the backend health status |
| `POST` | `/api/v1/analysis` | Runs a research request |

Interactive API documentation is available at <http://127.0.0.1:8000/docs> when the backend is running.

### Analysis request

```json
{
  "question": "Summarize the available financial information about Reliance Industries.",
  "ticker": "RELIANCE",
  "fiscal_year": null,
  "start_date": null,
  "end_date": null
}
```

The `question` field is required and must contain between 5 and 4,000 characters. The ticker is optional and must be supported by the backend. For a date range, provide both `start_date` and `end_date`; the end date must be later than the start date.

### Analysis response

```json
{
  "ticker": "RELIANCE",
  "fiscal_year": null,
  "report": "Research report text returned by the backend."
}
```

## Frontend commands

Run these commands from the `frontend` directory:

```bat
npm run dev      # Start the development server
npm run build    # Build the frontend
npm run preview  # Preview a production build
npm run lint     # Run the linter
```

## Team

- **Ayush Solanki** — Full Stack Developer; Coordination Support
- **Divyansh Pratap Singh** — AI/ML Developer
- **Ashwani Kumar** — Backend Developer
- **Dev Gupta** — Team Member; Research & Presentation

## Responsible use

FinSight is an educational research prototype, not personalized financial advice. Reports may be incomplete, delayed, or incorrect. Verify findings against official company filings and other reliable sources before making financial decisions.