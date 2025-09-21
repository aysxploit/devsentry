# 🛡️ DevSentry

**Live Demo:** [Streamlit - DevSentry](http://94.16.31.129:8505/)  
**Demo Video:** _Pending Submission_

---

## Overview

**DevSentry** is an end-to-end agentic AI system that acts as a senior developer's assistant for real-time **error triage and auto-fix generation**. Built with FastAPI, Streamlit, LangChain, and Gemini 1.5 Flash, it provides intelligent runtime diagnostics and code fix suggestions across Python, JS, C++, and Java.

---

## Use Case & Impact

Modern development workflows suffer from low MTTR (Mean Time To Repair). DevSentry solves this by analyzing logs or error messages and generating actionable fix patches with reasoning.

**Impact**:
- Speeds up debugging for developers.
- Ideal for DevOps pipelines.
- Scales across multiple languages.

---

## Architecture Diagram

```plaintext
+----------------+     HTTP     +-------------------+     LangChain     +------------------+
|  Streamlit UI  | <==========> | FastAPI Controller | <==============> | Gemini LLM Agent |
+----------------+              +-------------------+                   +------------------+
     ^                                 |
     |                                 v
     |                        +-------------------+
     |                        | GitHub API Client |
     |                        +-------------------+
     |
     v
+------------------+
| LangSmith Tracer |
+------------------+
```

---

## Agent Prompt Design

DevSentry uses LangChain's `initialize_agent()` with a ReAct-based reasoning agent on Gemini 1.5. The prompt includes:
- Language context
- Error traceback
- Code snippet
- Instructions to isolate root cause and generate fix

_Example Prompt Template_:
```
You are a senior software engineer. Given the traceback and code, identify the issue and generate a patch-ready fix. Explain why.
```

---

## Features

- Multi-language runtime error support
- Auto classification of severity (Low to Critical)
- Structured fix generator
- LangSmith trace visualization
- GitHub API integration (search relevant issues)

---

## Tooling / APIs Used

- `Gemini 1.5 Flash` via LangChain
- `GitHub REST API` (Issue similarity + references)
- `LangSmith` (observability)
- `FastAPI`, `Streamlit`

---

## Observability

- LangSmith Tracing (`LANGCHAIN_TRACING_V2`)
- Custom `uvicorn` structured logging (JSON)
- Logs persisted and visualized in LangSmith Dashboard

---

## Testing

Test suite located in `tests/`:
- `test_agent.py`: Unit test on error prompts
- `test_utils.py`: Unit test for utility transformers
- `test_api.py`: Integration test for `/analyze` endpoint

Run all tests:
```bash
pytest tests/
```

---

## Deployment

### Local Development
```bash
docker-compose up --build
```

### Manual
```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Streamlit:
```bash
streamlit run ui/dashboard.py
```

---

## Directory Structure

```
devsentry/
├── app/
│   ├── main.py         # FastAPI app
│   ├── agent.py        # LangChain agent
│   ├── fixgen.py       # Patch suggestion logic
│   ├── triage.py       # Severity classification
│   └── utils.py        # Support utilities
├── ui/
│   └── dashboard.py    # Streamlit frontend
├── tests/              # Pytest-based unit/integration tests
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## Authors
- **TwilightAshen3196**
