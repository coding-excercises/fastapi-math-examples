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
    response = client.get("/ai/sentiment?input_text=friends%20and%20i%20are%20very%20happy%20playing%20video%20games.%20but%20my%20parents%20and%20friends%20are%20not%20happy.&input_entity1=friends&input_entity2=parents")
    assert response.status_code == 200
    assert response.json() == ["Sentiment.positive","2","Sentiment.negative","1"]
