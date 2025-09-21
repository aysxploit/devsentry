import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.agent import process_error

# Structured Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

app = FastAPI()

class ErrorReport(BaseModel):
    error_message: str
    stack_trace: str
    language: str = "python"

@app.post("/analyze")
async def analyze_error(payload: ErrorReport):
    try:
        logging.info("Received request: %s", payload.dict())
        result = await process_error(payload)
        logging.info("Analysis complete.")
        return result
    except Exception as e:
        logging.exception("Error during processing")
        raise HTTPException(status_code=500, detail=str(e))
