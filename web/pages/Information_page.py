from selene import browser, have, query
import html

from utils.config_web import ABOUT_COMPANY_TEXT


class InformationPage:
    def cheking_about_company_text(self):
        actual_text = browser.element('#article_container_208044859').get(query.text)
        text = html.unescape(actual_text)
        text = ' '.join(text.split())

        assert text == ABOUT_COMPANY_TEXT

    def verify_successful_search(self, text):
        browser.element('#jsx-pet-app').should(have.text(f'"{text}" найден'))

    def verify_partial_match_search(self, text):
        browser.element('#jsx-pet-app').should(have.text(f'По запросу "{text}" точных совпадений не нашли.'))

    def verify_no_results_found(self):
        browser.element('.info-message').should(have.text('Мы не нашли подходящих товаров'))

    def verify_information_on_page(self, text):
        browser.element('.categories-title').should(have.text(text))


information_page = InformationPage()
