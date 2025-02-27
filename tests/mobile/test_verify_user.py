import allure
from models.mobile.mobile_app import PetrovichMobileApp
from utils.config_web import user_name, user_password


@allure.tag('mobile')
@allure.epic("Авторизация пользователя")
@allure.feature("Вход пользователя")
@allure.story("Успешная авторизация в системе")
@allure.title("Тест авторизации в приложении Петрович")
@allure.description("Этот тест проверяет возможность авторизации в мобильном приложении Петрович.")
@allure.label("owner", "Ярослав Гусев")
def test_verify_user(mobile_management):
    mobile = PetrovichMobileApp()

    with allure.step('Пропускаем начальные экраны'):
        mobile.skip_initial_screens(2)

    with allure.step('Выбираем город'):
        mobile.choice_city('Санкт-Петербург')

    with allure.step('Входим в аккаунт'):
        mobile.login(user_name, user_password)

    with allure.step('Проверяем, что перешли на главную страницу'):
        mobile.checking_home_page()

    with allure.step('Переходим в "Профиль"'):
        mobile.user_profile()

    with allure.step('Проверяем, что мы вошли в аккаунт'):
        mobile.verify_user()
