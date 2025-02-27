from selene import browser, by, be
from selenium.webdriver.common.action_chains import ActionChains


class CatalogPage:
    @staticmethod
    def open_catalog():
        browser.element('.catalog-button').should(be.clickable).click()

    @staticmethod
    def search_section(text):
        element = browser.element('.sections-menu-top').should(be.visible).element(by.text(text))
        actions = ActionChains(browser.driver)
        actions.move_to_element(element()).perform()

    @staticmethod
    def search_categories(text):
        browser.element('.sections-menu-content').element(by.text(text)).click()
