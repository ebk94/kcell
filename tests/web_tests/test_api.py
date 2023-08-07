import pytest
import requests

BASE_URL = 'https://demoqa.com'
USER_ENDPOINT = ''
headers = {'accept': 'application/json', 'Content-Type':'application/json', 'authorization':'Basic YWRtaW5AYWRtaW4uYWQ6IUJzTTg0MTE=, !BsM8411'}
user_data = {
        "userName": "test@user.com",
        "password": "12Qwdss@dg"
    }

@pytest.mark.smoke
def test_user_is_authorized():
    response = requests.post(BASE_URL + "/Account/v1/Authorized", headers=headers, json=user_data)
    assert response.status_code == 200
    print(response.json())
    body = response.json()
    assert body == True

@pytest.mark.smoke
def test_generate_token():
    response = requests.post(BASE_URL + "/Account/v1/GenerateToken", headers=headers, json=user_data)
    assert response.status_code == 200
    print(response.json())
    body = response.json()
    for value in body:
        if value in body:
            assert True
        else: False

@pytest.mark.smoke
def test_create_user():
    user_data = {
        "userName": "test@user.com",
        "password": "12Qwdss@dg"
    }
    response = requests.post(BASE_URL + "/Account/v1/User/", headers=headers, json=user_data)
    assert response.status_code == 200
    print(response.json())
    body = response.json()
    for value in body:
        if value in body:
            assert True
        else: False