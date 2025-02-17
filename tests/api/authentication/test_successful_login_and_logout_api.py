from models.api.authentication import Authentication
from models.api.cookie_manager import CookieManager
import allure

from models.pages.profile_page import ProfilePage
from models.pages.base_page import BasePage


@allure.epic("Авторизация пользователя")
@allure.feature("Вход и выход пользователя")
@allure.story("Успешная авторизация и выход из системы")
def test_successful_login_and_logout(browser_management):
    start = BasePage()
    cookie_manager = CookieManager()
    auth = Authentication()
    checking = ProfilePage()

    with allure.step("Открытие главной страницы"):
        start.open_main_page()

    with allure.step("Получение cookies из браузера"):
        cookie_manager.get_browser_cookies()

    with allure.step("Выполнение входа в систему"):
        auth.login()

    with allure.step('Переходим на вкладку профайла'):
        start.open_main_page()
        checking.choise_profile()

    with allure.step("Проверка личных данных пользователя в системе"):
        checking.checking_profile_user()

    with allure.step("Выполнение выхода из системы"):
        auth.logout()
