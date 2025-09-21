from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_scan_inline():
    r = client.post("/scan", data={"text": "password = 'secret'\nTODO: remove"})
    assert r.status_code == 200
    js = r.json()
    assert "findings" in js and len(js["findings"]) >= 1
