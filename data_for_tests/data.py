class Urls:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site/'
    REGISTER_URL = 'api/auth/register'
    LOGIN_URL = 'api/auth/login'
    USER_URL = 'api/auth/user'
    ORDERS_URL = 'api/orders'


class UserData:
    without_name = {"email": "koroleva_11@yandex.ru", "password": "11JH4520H"}
    without_email = {"password": "11JH4520H", "name": "Kate"}
    without_password = {"email": "kate@yandex.ru", "name": "Kate"}


class Ingredients:
    correct_ingredients = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa6d",
            "61c0c5a71d1f82001bdaaa73"
        ]
    }
    incorrect_ingredients = {
        "ingredients": [
            "bdaaa6d",
            "bdaaa73"
        ]
    }
