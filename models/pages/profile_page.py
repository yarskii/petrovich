from selene import browser, have, be
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class ProfilePage:
    def choise_profile(self):
        browser.element('[href="/cabinet/profile/"]').should(be.visible).click()

    def checking_profile_user(self):
        try:
            browser.element('.profile').should(have.text('Личные данные'))
            logging.info('Информация с личными данными найдена.')
        except Exception:
            logging.error('Элемент профиля не найден. Вы не авторизированны.')
