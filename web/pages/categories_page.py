from selene import browser, by, be


class CategoriesPage:
    @staticmethod
    def search_categories(text):
        products = browser.element('.sections-nav').should(be.visible)
        products.element(by.text(text)).click()
