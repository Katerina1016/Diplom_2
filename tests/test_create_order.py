import allure
import requests
from conftest import create_and_delete_user
from data_for_tests.data import Urls, Ingredients


class TestCreateOrder:
    @allure.title('Создание заказа авторизованным пользователем')
    @allure.description('Проверка ответа в формате JSON')
    def test_create_order_authorised_user_success(self, create_and_delete_user):
        token = {'Authorization': create_and_delete_user[3]}
        r = requests.post(Urls.MAIN_URL + Urls.ORDERS_URL, headers=token,
                          data=Ingredients.correct_ingredients)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.title('Cоздание заказа неавторизованным пользователем')
    @allure.description('Проверка ответа в формате JSON')
    def test_create_order_user_without_authorisation_success(self, create_and_delete_user):
        r = requests.post(Urls.MAIN_URL + Urls.ORDERS_URL, data=Ingredients.correct_ingredients)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.title('Оформление заказа без ингредиента')
    @allure.description('Проверка ответа в формате JSON')
    def test_create_order_without_ingredients_fail(self, create_and_delete_user):
        r = requests.post(Urls.MAIN_URL + Urls.ORDERS_URL)
        assert r.status_code == 400 and r.json()['message'] == "Ingredient ids must be provided"

    @allure.title('Оформление заказа с неверным ингредиентом')
    @allure.description('Проверка ответа в формате JSON')
    def test_create_order_incorrect_hash_fail(self, create_and_delete_user):
        r = requests.post(Urls.MAIN_URL + Urls.ORDERS_URL, data=Ingredients.incorrect_ingredients)
        assert r.status_code == 500 and 'Internal Server Error' in r.text
