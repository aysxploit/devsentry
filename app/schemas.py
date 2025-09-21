from pydantic import BaseModel

class ErrorReportSchema(BaseModel):
    error_message: str
    stack_trace: str
    language: str = "python"
