import allure
from models.mobile.mobile_app import PetrovichMobileApp
import pytest


@allure.tag('mobile')
@allure.epic("Вход пользователя в приложение")
@allure.feature("Вход пользователя без аутентификации")
@allure.story("Успешная вход в приложение")
@allure.title("Тест входа в приложении Петрович")
@allure.description("Этот тест проверяет возможность входа в мобильное приложении Петрович.")
@allure.label("owner", "Ярослав Гусев")
@pytest.mark.parametrize('mobile_management',
                         [('11.0', 'android', 'Samsung Galaxy S21')],
                         ids=['Samsung Galaxy S21'],
                         indirect=True)
def test_without_login(mobile_management):
    mobile = PetrovichMobileApp()

    with allure.step('Пропускаем начальные экраны'):
        mobile.skipping_start_settings()
        mobile.skipping_start_settings()

    with allure.step('Выбираем город'):
        mobile.choice_city('Санкт-Петербург')

    with allure.step('Выбираем вход без регистрации (нажимаем "В другой раз")'):
        mobile.enter_without_login()

    with allure.step('Проверяем, что перешли на главную страницу'):
        mobile.checking_home_page()

    with allure.step('Переходим в "Профиль"'):
        mobile.user_profile()

    with allure.step('Проверяем, что вход в аккаунт не произошел'):
        mobile.checking_enter()
