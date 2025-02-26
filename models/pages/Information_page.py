from selene import browser, have, be


class InformationPage:
    def cheking_about_company_text(self, text):
        browser.element('#article_container_208044859').should(be.visible).should(have.text(text))

    def verify_successful_search(self, text):
        browser.element('#jsx-pet-app').should(have.text(f'"{text}" найден'))

    def verify_partial_match_search(self, text):
        browser.element('#jsx-pet-app').should(have.text(f'По запросу "{text}" точных совпадений не нашли.'))

    def verify_no_results_found(self):
        browser.element('.info-message').should(have.text('Мы не нашли подходящих товаров'))

    def verify_information_on_page(self, text):
        browser.element('.categories-title').should(have.text(text))
