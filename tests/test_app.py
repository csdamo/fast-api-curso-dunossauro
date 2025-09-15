from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    # Arrange
    # client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_exercicio_02(client):
    # Arrange
    # client = TestClient(app)

    # Act
    response = client.get('/exercicio2')

    # Assert
    assert '<h1> Olá Mundo </h1>' in response.text
    assert response.status_code == HTTPStatus.OK
