from selene import browser, have, by, be
from utils.config_web import user_name, user_password


class LoginPage:
    def click_header_button(self):
        browser.element('.auth-header-button').should(have.text('Войти')).click()

    def enter_email(self):
        email_input = browser.element(by.xpath("//label[contains(., 'E-mail или логин')]/input"))
        email_input.should(be.visible)
        email_input.type(user_name)

    def enter_password(self):
        browser.element('.input-password').type(user_password)

    def click_submit_button(self):
        browser.element('.loginreg-form-submit-btn').should(be.visible).click()
