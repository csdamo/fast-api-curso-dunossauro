import pytest
from fastapi.testclient import TestClient

from fast_api_0.app import app


@pytest.fixture
def client():
    return TestClient(app)
