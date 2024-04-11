import pytest
from flask import Flask
from flask.testing import FlaskClient
from quiz import quiz

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page(client: FlaskClient):
    response = client.get('/')
    assert response.status_code == 200
    assert b'home.html' in response.data

def test_quiz_page(client: FlaskClient):
    response = client.get('/quiz/')
    assert response.status_code == 200
    assert b'quiz.html' in response.data