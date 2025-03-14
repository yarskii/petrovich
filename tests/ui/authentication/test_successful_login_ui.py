import allure

from web.components.navigation import Navigation
from web.pages.login_page import LoginPage
from web.pages.profile_page import ProfilePage


@allure.tag('web')
@allure.epic("Авторизация пользователя")
@allure.feature("Вход пользователя")
@allure.story("Успешная авторизация в системе")
@allure.label("owner", "Ярослав Гусев")
@allure.link("https://petrovich.ru/", name="Вход пользователя")
def test_successful_login(browser_management):
    login = LoginPage()

    with allure.step("Открытие главной страницы"):
        Navigation.open_home_page()

    with allure.step('Нажатие на кнопку "Войти"'):
        login.click_header_button()

    with allure.step('Ввод E-mail или логина'):
        login.enter_email()

    with allure.step('Ввод пароля'):
        login.enter_password()

    with allure.step('Нажатие на кнопку "Войти" для авторизации'):
        login.click_submit_button()

    with allure.step('Переход на вкладку профиля'):
        ProfilePage.choice_profile()

    with allure.step('Проверка личных данных пользователя в системе'):
        ProfilePage.checking_profile_user()
