from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "version": "0.1.0"
    }


def test_family_sedan_recommendation():
    response = client.post(
        "/recommend",
        json={
            "body_type": "sedan",
            "family": True
        }
    )

    assert response.status_code == 200
    assert response.json()["recommendation"] == "Superb"


def test_sedan_recommendation():
    response = client.post(
        "/recommend",
        json={
            "body_type": "sedan",
            "family": False
        }
    )

    assert response.status_code == 200
    assert response.json()["recommendation"] == "Octavia"


def test_suv_recommendation():
    response = client.post(
        "/recommend",
        json={
            "body_type": "suv",
            "family": False
        }
    )

    assert response.status_code == 200
    assert response.json()["recommendation"] == "Kodiaq"


def test_invalid_request():
    response = client.post(
        "/recommend",
        json={
            "body_type": 123,
            "family": "abc"
        }
    )

    assert response.status_code == 422