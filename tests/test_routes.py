from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_detect_text():
    response = client.post("/ai-detection/text", json={"text": "Hello, AI!"})
    assert response.status_code == 200

def test_detect_image():
    response = client.post("/ai-detection/image", files={"file": ("test.png", open("test_image.png", "rb"))})
    assert response.status_code == 200
