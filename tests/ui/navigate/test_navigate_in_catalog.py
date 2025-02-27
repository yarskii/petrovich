import pytest
import allure

from web.components.navigation import Navigation
from web.pages.Information_page import information_page
from web.pages.catalog_page import CatalogPage


@allure.tag('web')
@allure.feature('Каталог товаров')
@allure.story('Переход в категорию каталога')
@allure.title('Проверка перехода в подкатегорию')
@allure.label("owner", "Ярослав Гусев")
@allure.description(
    'Тест проверяет возможность перехода в подкатегорию через основной раздел')
@allure.link("https://petrovich.ru/", name="Главная страница магазина")
@pytest.mark.parametrize(('section', 'title'),
                         [('Товары для дома', 'Стеклоочистители'), ('Электрика', 'Лампы')],
                         ids=['Tovari dlya doma', 'Electrica'])
def test_navigate_in_catalog(browser_management, section, title):
    with allure.step('Открываем главную страницу магазина'):
        Navigation.open_home_page()

    with allure.step('Открываем каталог товаров'):
        CatalogPage.open_catalog()

    with allure.step(f'Находим раздел "{section}" в каталоге'):
        CatalogPage.search_section(section)

    with allure.step(f'Выбираем категорию "{title}"'):
        CatalogPage.search_categories(title)

    with allure.step(f'Проверяем, что открылась страница категории "{title}"'):
        information_page.verify_information_on_page(title)
