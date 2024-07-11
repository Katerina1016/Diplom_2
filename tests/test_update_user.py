import pytest
import allure
import requests
from conftest import create_and_delete_user
from data_for_tests.data import Urls
from helpers.helpers import generate_random_string


class TestChangeUserData:
    @allure.title('Тест изменение почты авторизованного пользователя')
    @allure.description('Проверка статус кода и ответа в формате JSON')
    def test_change_user_email_authorised_user_success(self, create_and_delete_user):
        new_email = f'{generate_random_string(5)}@yandex.ru'
        payload = {'email': new_email}
        token = {'Authorization': create_and_delete_user[3]}
        r = requests.patch(Urls.MAIN_URL + Urls.USER_URL, headers=token, data=payload)
        assert r.status_code == 200 and r.json()['user']['email'] == new_email

    @allure.title('Тест изменение пароля авторизованного пользователя')
    @allure.description('Проверка статус кода и ответа в формате JSON')
    def test_change_user_password_authorised_user_success(self, create_and_delete_user):
        new_password = generate_random_string(5)
        payload = {'password': new_password}
        token = {'Authorization': create_and_delete_user[3]}
        r = requests.patch(Urls.MAIN_URL + Urls.USER_URL, headers=token, data=payload)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.title('Тест изменение имени авторизованного пользователя')
    @allure.description('Проверка статус кода и ответа в формате JSON')
    def test_change_user_name_authorised_user_success(self, create_and_delete_user):
        new_name = generate_random_string(5)
        payload = {'name': new_name}
        token = {'Authorization': create_and_delete_user[3]}
        response = requests.patch(Urls.MAIN_URL + Urls.USER_URL, headers=token, data=payload)
        assert response.status_code == 200 and response.json()['user']['name'] == new_name

    @allure.title('Тест обновление данных неавторизованного пользователя')
    @allure.description('Проверка статус кода и ответа в формате JSON')
    @pytest.mark.parametrize('payload', [{'email': f'{generate_random_string(5)}@mail.ru'},
                                         {'password': generate_random_string(5)},
                                         {'name':  generate_random_string(5)}])
    def test_change_user_data_without_authorization_fail(self, payload):
        r = requests.patch(Urls.MAIN_URL + Urls.USER_URL, data=payload)
        assert r.status_code == 401 and r.json()['message'] == 'You should be authorised'
