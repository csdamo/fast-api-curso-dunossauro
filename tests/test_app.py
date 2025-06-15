from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api_0.app import app


def test_root_deve_retornar_ola_mundo():
    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Olá mundo'}
    assert response.status_code == HTTPStatus.OK
