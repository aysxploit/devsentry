import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_post_analyze():
    response = client.post("/analyze", json={
        "error_message": "ZeroDivisionError: division by zero",
        "stack_trace": "File 'main.py', line 5",
        "language": "python"
    })
    assert response.status_code == 200
    data = response.json()
    assert "classification" in data
    assert "fix_suggestion" in data
