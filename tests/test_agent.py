import pytest
from app.schemas import ErrorReportSchema
from app.agent import process_error
import asyncio

@pytest.mark.asyncio
async def test_process_error_basic():
    report = ErrorReportSchema(
        error_message="TypeError: unsupported operand type(s)",
        stack_trace="File 'main.py', line 2",
        language="python"
    )
    result = await process_error(report)
    assert "classification" in result
    assert "fix_suggestion" in result
