from __future__ import annotations
import os
from typing import Optional

def summarize(prompt: str, context: Optional[str] = None) -> str:
    key = os.getenv("GEMINI_API_KEY", "").strip()
    if not key:
        base = (context or "")[:4000]
        return f"AI not configured. Echo summary:\n{prompt[:500]}\n\nContext:\n{base}"
    try:
        import google.generativeai as genai
        genai.configure(api_key=key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        full_prompt = (
            "You are DevSentry assistant. Summarize or propose remediations for security findings.\n"
            f"User prompt: {prompt}\nContext (may include findings):\n{context or ''}\n"
            "Return a concise, actionable response."
        )
        resp = model.generate_content(full_prompt)
        return (resp.text or "").strip() or "No response."
    except Exception as e:
        return f"AI error: {e}"
