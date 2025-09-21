# DevSentry

FastAPI backend + Streamlit UI for lightweight code scanning, AI-assisted triage, and conversation around findings.
This version targets **Python 3.13**, updates dependencies, and adopts **Pydantic v2** models and **FastAPI 0.115** style.

## Features
- `/health` endpoint for readiness checks.
- `/scan` endpoint: uploads code/text and returns security findings (simple secret/credential heuristics + TODO/FIXME).
- `/chat` endpoint: optional Gemini-backed assistant to summarize findings or suggest remediations.
- Streamlit UI: upload files/folders (zips), see findings, chat about them.
- Dockerfile based on `python:3.13-slim`.

## Run (dev)
```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
UI:
```bash
streamlit run ui/streamlit_app.py
```

## Env
Create `.env` in project root:
```
GEMINI_API_KEY=
BACKEND_URL=http://localhost:8000
```

## Docker
```bash
docker build -t devsentry:py313 .
docker run --rm -p 8000:8000 devsentry:py313
```

## Tests
```bash
pytest -q
```

## Notes
- AI is optional; scanning works offline.
- This modernization preserves the intended DevSentry workflow while upgrading to Python 3.13-compatible libs.
