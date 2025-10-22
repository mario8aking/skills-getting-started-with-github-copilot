import pytest
from fastapi.testclient import TestClient
from src.app import app, activities

client = TestClient(app)


def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "participants" in data["Chess Club"]


def test_signup_for_activity():
    test_email = "pytestuser@mergington.edu"
    activity = "Chess Club"
    # Remove if already present
    if test_email in activities[activity]["participants"]:
        activities[activity]["participants"].remove(test_email)
    response = client.post(f"/activities/{activity}/signup?email={test_email}")
    assert response.status_code == 200
    assert test_email in activities[activity]["participants"]


def test_unregister_for_activity():
    test_email = "pytestuser@mergington.edu"
    activity = "Chess Club"
    # Add if not present
    if test_email not in activities[activity]["participants"]:
        activities[activity]["participants"].append(test_email)
    # Simulate unregister endpoint (should exist in app)
    response = client.post(f"/activities/{activity}/unregister?email={test_email}")
    assert response.status_code == 200
    assert test_email not in activities[activity]["participants"]
