from selene import browser


class CookieManager:
    def get_browser_cookies(self):
        selenium_cookies = browser.driver.get_cookies()
        return {cookie['name']: cookie['value'] for cookie in selenium_cookies}
