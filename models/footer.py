from selene import browser, be


class Footer:
    @staticmethod
    def about_company():
        button = browser.element('[href="/about/"]').should(be.visible)
        button.should(be.clickable).click()
