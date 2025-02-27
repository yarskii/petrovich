from selene import browser, have, be
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class ProfilePage:
    @staticmethod
    def choice_profile():
        browser.element('[href="/cabinet/profile/"]').should(be.visible).click()

    @staticmethod
    def checking_profile_user():
        try:
            browser.element('.profile').should(have.text('Личные данные'))
            logging.info('Информация с личными данными найдена.')
        except Exception:
            logging.error('Элемент профиля не найден. Вы не авторизированны.')
