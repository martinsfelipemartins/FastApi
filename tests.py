from starlette.testclient import TestClient

from main import app   

client =  TestClient(app)

def test_main_status_code():
    responde = client.get("/todo")
    assert responde.status_code == 200

def test_main_response_json():
    response = client.get("/todo")
    assert len(response.json()) == 2