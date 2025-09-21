from __future__ import annotations
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from .models import HealthResponse, ScanItem, ScanResponse, ChatRequest, ChatResponse
from .security.scanner import scan_text
from .ai import summarize

VERSION = "0.2.0-py313"

app = FastAPI(title="DevSentry", version=VERSION)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", version=VERSION)

@app.post("/scan", response_model=ScanResponse)
async def scan(
    text: Optional[str] = Form(default=None),
    files: List[UploadFile] | None = None,
) -> ScanResponse:
    findings: List[ScanItem] = []

    if text:
        for path, line, desc, sev, snippet in scan_text("inline.txt", text):
            findings.append(ScanItem(path=path, line=line, issue=desc, severity=sev, snippet=snippet))

    for f in (files or []):
        try:
            content = (await f.read()).decode("utf-8", errors="ignore")
            for path, line, desc, sev, snippet in scan_text(f.filename, content):
                findings.append(ScanItem(path=path, line=line, issue=desc, severity=sev, snippet=snippet))
        finally:
            await f.aclose()

    return ScanResponse(findings=findings)

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest) -> ChatResponse:
    ans = summarize(req.prompt, req.context)
    return ChatResponse(answer=ans)
