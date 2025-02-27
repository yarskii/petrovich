from api.models.authentication import Authentication
from api.models.cookie_manager import CookieManager
import allure

from web.components.navigation import Navigation
from web.pages.profile_page import ProfilePage


@allure.epic("Авторизация пользователя")
@allure.feature("Вход и выход пользователя")
@allure.story("Успешная авторизация и выход из системы")
def test_successful_login_and_logout(browser_management):
    auth = Authentication()

    with allure.step("Открытие главной страницы"):
        Navigation.open_home_page()

    with allure.step("Получение cookies из браузера"):
        CookieManager.get_browser_cookies()

    with allure.step("Выполнение входа в систему"):
        auth.login()

    with allure.step('Переходим на вкладку профайла'):
        Navigation.open_home_page()
        ProfilePage.choice_profile()

    with allure.step("Проверка личных данных пользователя в системе"):
        ProfilePage.checking_profile_user()

    with allure.step("Выполнение выхода из системы"):
        auth.logout()
