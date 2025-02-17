from selene import browser, by, be


class CategoriesPage:
    def search_categories(self, text):
        products = browser.element('.sections-nav').should(be.visible)
        products.element(by.text(text)).click()
