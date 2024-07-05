import allure
import requests
from conftest import create_and_delete_user
from data_for_tests.data import Urls
from helpers.helpers import create_user_login


class TestLoginUser:
    @allure.title('Тест авторизация пользователя без ошибок')
    @allure.description('Проверка статус кода и ответа в формате JSON')
    def test_user_login_success(self, create_and_delete_user):
        r = requests.post(Urls.MAIN_URL + Urls.LOGIN_URL, data=create_and_delete_user[2])
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.title('Тест авторизация пользователя с неверным логином и паролем')
    @allure.description('Проверка статус кода и ответа в формате JSON')
    def test_user_login_incorrect_login_data_fail(self, create_and_delete_user):
        payload = create_user_login()
        r = requests.post(Urls.MAIN_URL + Urls.LOGIN_URL, data=payload)
        assert r.status_code == 401 and r.json()['message'] == "email or password are incorrect"
