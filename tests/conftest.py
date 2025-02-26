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
DEFAULT_MOBILE_ENVIRONMENT = 'browserstack'
DEFAULT_WEB_ENVIRONMENT = 'local'


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default=DEFAULT_BROWSER_VERSION
    )
    parser.addoption(
        '--mobile_env',
        default=DEFAULT_MOBILE_ENVIRONMENT
    )
    parser.addoption(
        '--web_env',
        default=DEFAULT_WEB_ENVIRONMENT
    )


@pytest.fixture(scope='function')
def browser_management(request):
    base_url = os.getenv('BASE_URL')
    browser_version = request.config.getoption('browser_version') or DEFAULT_BROWSER_VERSION
    web_env = request.config.getoption('web_env') or DEFAULT_WEB_ENVIRONMENT

    driver_options = webdriver.ChromeOptions()

    if web_env == 'local':
        driver_options.page_load_strategy = 'eager'
        driver_options.add_argument('--headless')
        driver_options.add_argument('--disable-gpu')
        driver_options.add_argument('--no-sandbox')

    else:
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

        driver_options.page_load_strategy = 'eager'
        browser.config.window_height = 1080
        browser.config.window_width = 1920

    browser.config.driver_options = driver_options
    browser.config.base_url = base_url
    browser.config.timeout = float(os.getenv('timeout', '15.0'))

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture(scope='function',
                params=[('15.0', 'android', 'Google Pixel 9')],
                ids=['base'])
def mobile_management(request):
    mobile_env = request.config.getoption('mobile_env') or DEFAULT_MOBILE_ENVIRONMENT

    with allure.step('Инициализация сессии приложения'):
        if mobile_env == 'local':
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
