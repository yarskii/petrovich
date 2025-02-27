from selene import browser, be


class ProductUI:
    @staticmethod
    def search_product(text):
        product = browser.element('.header-search-input').should(be.visible)
        product.type(text).press_enter()
