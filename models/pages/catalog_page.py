from selene import browser, by, be
from selenium.webdriver.common.action_chains import ActionChains


class CatalogPage:
    def open_catalog(self):
        browser.element('.catalog-button').should(be.clickable).click()

    def search_section(self, text):
        element = browser.element('.sections-menu-top').should(be.visible).element(by.text(text))
        actions = ActionChains(browser.driver)
        actions.move_to_element(element()).perform()

    def search_categories(self, text):
        browser.element('.sections-menu-content').element(by.text(text)).click()
