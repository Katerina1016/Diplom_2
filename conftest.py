import pytest
from helpers.helpers import *
from data_for_tests.data import Urls
import requests


@pytest.fixture(scope="function")
def create_and_delete_user():
    payload = create_user_data()
    login_data = payload.copy()
    del login_data["name"]
    response = requests.post(Urls.MAIN_URL+Urls.REGISTER_URL, data=payload)
    token = response.json()["accessToken"]
    yield response, payload, login_data, token
    requests.delete(Urls.MAIN_URL + Urls.USER_URL, headers={'Authorization': f'{token}'})
