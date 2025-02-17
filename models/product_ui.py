from selene import browser, be


class ProductUI:
    def search_product(self, text):
        product = browser.element('.header-search-input').should(be.visible)
        product.type(text).press_enter()
