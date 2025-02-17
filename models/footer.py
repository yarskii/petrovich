from selene import browser


class Footer:
    def about_company(self):
        browser.element('[href="/about/"]').click()
