from fastapi.testclient import TestClient
from main import app  # your FastAPI app


client = TestClient(app)


def test_create_job(mocker):
    # Mock Redis
    mock_redis = mocker.patch("main.r")
    mock_redis.lpush.return_value = 1
    mock_redis.hset.return_value = 1

    response = client.post("/jobs")
    assert response.status_code == 200
    assert "job_id" in response.json()
    mock_redis.lpush.assert_called_once()
    mock_redis.hset.assert_called_once()


def test_get_job_not_found(mocker):
    mock_redis = mocker.patch("main.r")
    mock_redis.hget.return_value = None

    response = client.get("/jobs/nonexistent")
    assert response.status_code == 404


def test_get_job_found(mocker):
    mock_redis = mocker.patch("main.r")
    mock_redis.hget.return_value = "queued"

    response = client.get("/jobs/123")
    assert response.status_code == 200
    assert response.json()["status"] == "queued"
