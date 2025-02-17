import allure
from selene import browser
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
from utils import config_mobile
from appium import webdriver as appium

from utils import attach

load_dotenv()
DEFAULT_BROWSER_VERSION = '126.0'
DEFAULT_MOBILE_ENV = 'browserstack'


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default=DEFAULT_BROWSER_VERSION)
    parser.addoption(
        '--env',
        default=DEFAULT_MOBILE_ENV
    )


@pytest.fixture(scope='function')
def browser_management(request):
    browser_version = request.config.getoption('browser_version') or DEFAULT_BROWSER_VERSION

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options,
        keep_alive=True
    )

    browser.config.driver = driver

    driver_options = webdriver.ChromeOptions()

    driver_options.page_load_strategy = 'eager'
    driver_options.add_argument('--window-size=1280,724')

    browser.config.driver_options = driver_options
    browser.config.base_url = 'https://petrovich.ru'

    yield driver

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    driver.quit()


@pytest.fixture(scope='function',
                params=[('15.0', 'android', 'Google Pixel 9')],
                ids=['base'])
def mobile_management(request):
    env = request.config.getoption('env') or DEFAULT_MOBILE_ENV

    with allure.step('Инициализация сессии приложения'):
        if env == 'local':
            browser.config.driver = appium.Remote(
                config_mobile.remote_url,
                options=config_mobile.to_driver_options_local()
            )
        else:
            platform_version, platform_name, device_name = request.param
            browser.config.driver = appium.Remote(
                config_mobile.remote_url_bstack,
                options=config_mobile.to_driver_options_bstack(platform_version, platform_name, device_name)
            )

    browser.config.timeout = float(os.getenv('timeout', '30.0'))

    yield

    with allure.step('Закрытие мобильной сессии'):
        browser.quit()

# @pytest.fixture(scope='session', autouse=True)
# def browser_management():
#     driver_options = webdriver.ChromeOptions()
#
#     driver_options.page_load_strategy = 'eager'
#     driver_options.add_argument('--headless')
#     driver_options.add_argument('--disable-gpu')
#     driver_options.add_argument('--no-sandbox')
#     # driver_options.add_argument('--window-size=1280,724')
#
#     browser.config.driver_options = driver_options
#     browser.config.base_url = 'https://petrovich.ru'
#
#     yield
#     with allure.step('Закрытие браузера'):
#         if browser.config.driver and browser.config.driver.session_id:
#             browser.quit()
