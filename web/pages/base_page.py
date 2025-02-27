from selene import browser, have
import logging

logging.basicConfig(level=logging.INFO)


class BasePage:
    @staticmethod
    def search_section(text):
        browser.all('.header-nav-sections').element_by(have.text(text)).click()
