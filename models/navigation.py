from selene import browser
from utils.config_web import base_url


class Navigation:
    @staticmethod
    def open_home_page():
        browser.open('/')

    @staticmethod
    def open_categories_page():
        browser.open(f'{base_url}/catalog/778')
