from selene import browser
from utils.config_web import base_url


class Navigation:
    @staticmethod
    def open_home_page():
        browser.open_home_page('/')

    @staticmethod
    def open_categories_page():
        browser.open_home_page(f'{base_url}/catalog/778')
