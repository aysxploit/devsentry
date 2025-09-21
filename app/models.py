from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List, Optional

class HealthResponse(BaseModel):
    status: str = "ok"
    version: str = Field(..., description="Service version")

class ScanItem(BaseModel):
    path: str
    line: int
    issue: str
    severity: str = Field(default="info", pattern="^(info|low|medium|high)$")
    snippet: str

class ScanRequest(BaseModel):
    text: Optional[str] = None

class ScanResponse(BaseModel):
    findings: List[ScanItem]

class ChatRequest(BaseModel):
    prompt: str
    context: Optional[str] = None

class ChatResponse(BaseModel):
    answer: str
