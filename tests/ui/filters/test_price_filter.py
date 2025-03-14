import time
import allure
import pytest

from web.components.navigation import Navigation
from web.components.filters import PriceFilter


@allure.tag('web')
@allure.feature('Фильтры каталога')
@allure.story('Фильтр по цене')
@allure.title('Проверка фильтрации товаров по цене "От" и "До"')
@allure.label("owner", "Ярослав Гусев")
@allure.description('Тест проверяет возможность установить диапазон цен через фильтр "Цена, руб".')
@allure.link("https://petrovich.ru/", name="Страница каталога")
@pytest.mark.parametrize("min_price, max_price",
                         [('200', '1000'), ('500', '1500'), ('1000', '2000')])
def test_price_filter(browser_management, min_price, max_price):
    price = PriceFilter()

    with allure.step('Открываем страницу каталога'):
        Navigation.open_categories_page()
        # Использование time.sleep для ожидания завершения анимации/загрузки.
        time.sleep(2)

    with allure.step(f'Вводим минимальную цену ({min_price})'):
        price.set_min_price(min_price)
        # Использование time.sleep для ожидания завершения анимации/загрузки.
        time.sleep(2)

    with allure.step(f'Вводим максимальную цену ({max_price})'):
        price.set_max_price(max_price)

    with allure.step('Проверяем отображение диапазона цен'):
        price.checking_price_filter(min_price, max_price)
