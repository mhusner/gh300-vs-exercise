"""Shared pytest fixtures for backend API tests."""

from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


_INITIAL_ACTIVITIES = deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory activity state for deterministic test runs."""
    activities.clear()
    activities.update(deepcopy(_INITIAL_ACTIVITIES))
    yield
    activities.clear()
    activities.update(deepcopy(_INITIAL_ACTIVITIES))


@pytest.fixture
def client():
    """Return a test client for the FastAPI app."""
    return TestClient(app)
