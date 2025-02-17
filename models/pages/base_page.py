from selene import browser, have
import logging

logging.basicConfig(level=logging.INFO)


class BasePage:
    def open_main_page(self, url='/'):
        if url == '/':
            logging.info(f"Открываю главную страницу страницу")
        else:
            logging.info(f"Открываю страницу: {url}")
        browser.open(url)

    def search_section(self, text):
        browser.all('.header-nav-sections').element_by(have.text(text)).click()
