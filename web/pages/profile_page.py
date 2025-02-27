from selene import browser, have, be, by
import logging

from utils.config_web import user_name

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class ProfilePage:
    @staticmethod
    def choice_profile():
        browser.element('[href="/cabinet/profile/"]').should(be.visible).click()

    @staticmethod
    def checking_profile_user():
        try:
            name = browser.element(by.xpath("//label[contains(., 'Имя *')]/input"))
            name.should(be.visible).should(have.value(user_name.split('@')[0]))
            mail = browser.element(by.xpath("//label[contains(., 'E-mail *')]/input"))
            mail.should(be.visible).should(have.value(user_name))

            logging.info(f'Имя пользователя {user_name.split('@')[0]} и почта корректно отображаются в профиле.')
        except Exception:
            logging.error('Элемент профиля не найден. Вы не авторизированны.')
