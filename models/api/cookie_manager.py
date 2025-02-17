from selene import browser


class CookieManager:
    def get_browser_cookies(self):
        selenium_cookies = browser.driver.get_cookies()
        requests_cookies = {}
        for cookie in selenium_cookies:
            requests_cookies[cookie['name']] = cookie['value']

        return requests_cookies
