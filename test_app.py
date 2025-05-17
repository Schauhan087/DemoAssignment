import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Instagram Caption Generator' in response.data

def test_generate_caption(client):
    response = client.post('/generate', data={'category': 'nature'})
    assert response.status_code == 200
    assert b'Instagram Caption Generator' in response.data
    # At least one of our captions should be present
    assert (b'Lost in nature' in response.data or 
            b'Sunsets and good vibes' in response.data or 
            b'The mountains are calling' in response.data or 
            b'Take only pictures' in response.data)