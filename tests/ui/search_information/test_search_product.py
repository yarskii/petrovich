import pytest
import allure

from web.components.navigation import Navigation
from web.pages.Information_page import information_page
from web.components.product_ui import ProductUI


@allure.tag('web')
@allure.feature('Поиск товаров')
@allure.story('Успешный поиск существующего товара')
@allure.title('Проверка поиска существующего товара')
@allure.label("owner", "Ярослав Гусев")
@allure.description('Тест проверяет успешный поиск товара с корректным названием.')
@allure.link("https://petrovich.ru", name="Testing")
@pytest.mark.parametrize('title', ['Шуруповерт', 'Отвертка'],
                         ids=['Shurupovert', 'Otvertka'])
def test_successful_product_search(browser_management, title):
    with allure.step('Открываем главную страницу магазина.'):
        Navigation.open_home_page()

    with allure.step('В поисковую строку вводим корректное название товара.'):
        ProductUI.search_product(title)

    with allure.step('Проверяем, что найдены товары, соответствующие запросу'):
        information_page.verify_successful_search(title)


@allure.tag('web')
@allure.feature('Поиск товаров')
@allure.story('Поиск с частичным совпадением')
@allure.title('Проверка поиска товара с опечаткой')
@allure.label("owner", "Ярослав Гусев")
@allure.description('Тест проверяет случай, когда пользователь вводит название товара с ошибкой.')
@allure.link("https://petrovich.ru", name="Testing")
@pytest.mark.parametrize('title', ['Шараповерт', 'Адвертка'],
                         ids=['Sharapovert', 'Advertka'])
def test_partial_match_product_search(browser_management, title):
    with allure.step('Открываем главную страницу магазина.'):
        Navigation.open_home_page()

    with allure.step('В поисковую строку вводим название товара с опечаткой.'):
        ProductUI.search_product(title)

    with allure.step('Проверяем, что система предупреждает об отсутствии точных совпадений'):
        information_page.verify_partial_match_search(title)


@allure.tag('web')
@allure.feature('Поиск товаров')
@allure.story('Неудачный поиск')
@allure.title('Проверка поиска несуществующего товара')
@allure.label("owner", "Ярослав Гусев")
@allure.description('Тест проверяет случай, когда пользователь ищет несуществующий товар.')
@allure.link("https://petrovich.ru", name="Testing")
@pytest.mark.parametrize('title', ['sdjasdkjkjhaks'])
def test_failed_product_search(browser_management, title):
    with allure.step('Открываем главную страницу магазина.'):
        Navigation.open_home_page()

    with allure.step('В поисковую строку вводим название товара с опечаткой.'):
        ProductUI.search_product(title)

    with allure.step('Проверяем, что система сообщает об отсутствии подходящих товаров'):
        information_page.verify_no_results_found()
