from flask_todo import create_app

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_complete(client):
    response = client.get('/complete')
    assert response.status_code == 200
