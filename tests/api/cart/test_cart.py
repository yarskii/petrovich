from api.models.cart import Cart
from api.models.cookie_manager import CookieManager
import allure

from api.models.product_api import ProductAPI
from web.components.navigation import Navigation


def test_cart(browser_management):
    products_api = ProductAPI()
    cart = Cart()

    with allure.step("Открытие главной страницы"):
        Navigation.open_home_page()

    with allure.step("Получение cookies из браузера"):
        CookieManager.get_browser_cookies()

    with allure.step("Выбираем секцию"):
        section = products_api.get_sections()

    with allure.step(f'Получение продуктов из раздела {section[1]}'):
        product_guids = products_api.get_product_guids_in_section(section[0])

    with allure.step("Добавление продуктов в корзину"):
        products_api.add_product_in_cart(product_guids)

    with allure.step('Проверка содержимого корзины'):
        assert cart.checking_products_cart() > 0, "Корзина пуста."
