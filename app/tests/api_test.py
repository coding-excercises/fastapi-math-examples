from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_main():
    """Test the API main controller."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "FastAPI Math Examples"


def test_get_health():
    """Test the API health controller."""
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json() == "ok"


def test_get_add():
    """Test the API math add controller."""
    response = client.get("/math/add?a=5&b=5")
    assert response.status_code == 200
    assert response.json() == 10


def test_get_currency():
    """Test the API util currency controller."""
    response = client.get("/util/currency?from_curr=USD&to_curr=INR&amt=1")
    assert response.status_code == 200
    assert response.json() >= 70


def test_get_sentiment():
    """Test the API ai sentiment controller."""
    response = client.get("/ai/sentiment?input_text=Company%20shares%20are%20going%20up.%20But%2C%20employees%20are%20unhappy.")
    assert response.status_code == 200
    assert response.json() == {"neg": 0.301,"neu": 0.569,"pos": 0.13,"compound": -0.4767}
