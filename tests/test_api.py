import requests

BASE_URL = "http://35.154.1.53:32500"

def test_health_endpoint():
    r = requests.get(f"{BASE_URL}/health", timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "healthy"
    assert "model_version" in data

def test_predict_returns_label_and_confidence():
    r = requests.post(
        f"{BASE_URL}/predict",
        json={"text": "Spotlessly clean rooms with attentive staff and superb amenities throughout"},
        timeout=20
    )
    assert r.status_code == 200
    data = r.json()
    assert data["label"] in ["POSITIVE", "NEGATIVE"]
    assert 0 <= data["confidence"] <= 1
    assert "model_version" in data

def test_predict_negative_text():
    r = requests.post(
        f"{BASE_URL}/predict",
        json={"text": "The hotel room was terrible and the service was awful"},
        timeout=20
    )
    assert r.status_code == 200

def test_health_returns_model_version_unstable():
    r = requests.get(f"{BASE_URL}/health", timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert data["model_version"] == "unstable-v1"
