from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_api_status():
    response = client.get("/api/status")
    assert response.status_code == 200
    data = response.json()
    assert "agents" in data
    assert len(data["agents"]) > 0

def test_api_teach():
    payload = {
        "text": "Introduction to Neural Networks",
        "complexity": 0.5,
        "skills_req": {"logic": 0.6, "math": 0.4}
    }
    response = client.post("/api/teach", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "tick" in data
    assert "agents" in data

def test_api_train():
    response = client.post("/api/train")
    assert response.status_code == 200
    data = response.json()
    assert "final_loss" in data
    assert "epochs" in data

def test_api_metrics():
    response = client.get("/api/metrics")
    assert response.status_code == 200
    data = response.json()
    assert "gpa" in data
    assert "classroom_entropy" not in data # It's diversity_index now
    assert "diversity_index" in data

def test_api_graph():
    response = client.get("/api/graph")
    assert response.status_code == 200
    data = response.json()
    assert "nodes" in data
    assert "edges" in data
