from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser
from allure import step
import logging

logging.basicConfig(level=logging.INFO)


class PetrovichMobileApp:
    def skip_initial_screens(self, quantity):
        with step('Пропускаем экран'):
            for i in range(quantity):
                logging.info(f'Пропускаем экран {i + 1} из {quantity}')
                browser.element((AppiumBy.ID, 'ru.handh.petrovich:id/buttonAction')).should(
                    be.visible).click()

    def choice_city(self, city):
        with step('Отказываемся от определения местоположения'):
            browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')).should(
                be.visible).click()

        with step('Нажимаем кнопку "Выбрать город"'):
            browser.element((AppiumBy.ID, 'ru.handh.petrovich:id/buttonAnotherCity')).should(
                be.visible).click()

        with step('Вводим название города'):
            browser.element((AppiumBy.ID, 'ru.handh.petrovich:id/textInputEditTextSearch')).should(
                be.visible).type(city)

        with step('Выбираем первый город в списке'):
            first_article = browser.all((AppiumBy.ID, 'ru.handh.petrovich:id/linearLayoutContent')).first
            first_article.click()

        with step('Нажимаем кнопку "Продолжить"'):
            browser.element((AppiumBy.ID, 'ru.handh.petrovich:id/statefulButtonProceed')).should(
                be.visible).click()

    def login(self, login, password):
        with step('Нажимаем кнопку "Войти в аккаунт"'):
            browser.element((AppiumBy.ID, 'ru.handh.petrovich:id/buttonSignIn')).should(
                be.visible).click()

        with step('Выбираем "Войти по e-mail или логину"'):
            browser.element((AppiumBy.ID, 'ru.handh.petrovich:id/buttonSignInByEmailOrLogin')).should(
                be.visible).click()

        with step('Вводим E-mail или логин и пароль'):
            browser.element((AppiumBy.ID, 'ru.handh.petrovich:id/editTextEmailOrLogin')).should(
                be.visible).type(login)
            browser.element((AppiumBy.ID, 'ru.handh.petrovich:id/editTextPassword')).should(
                be.visible).type(password)

        with step('Нажимаем кнопку "Войти"'):
            browser.element((AppiumBy.ID, 'ru.handh.petrovich:id/buttonSignIn')).should(
                be.visible).click()

    def user_profile(self):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Профиль')).should(be.visible).click()

    def verify_user(self):
        browser.element((AppiumBy.ID, 'ru.handh.petrovich:id/textViewUserName')).should(
            have.text('tofol53249'))

    def checking_home_page(self):
        element = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Главная')).should(be.visible)
        element.should(have.attribute('selected').value('true'))

    def enter_without_login(self):
        browser.element((AppiumBy.ID, 'ru.handh.petrovich:id/buttonAnotherTime')).should(
            be.visible).click()

    def checking_enter(self):
        browser.element((AppiumBy.ID, 'ru.handh.petrovich:id/textViewTitle')).should(
            have.text('Войдите в профиль'))