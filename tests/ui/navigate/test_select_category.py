import pytest
import allure

from models.navigation import Navigation
from models.pages.Information_page import information_page
from models.pages.base_page import BasePage
from models.pages.categories_page import CategoriesPage


@allure.tag('web')
@allure.story('Переход в категорию через главную страницу')
@allure.label("owner", "Ярослав Гусев")
@allure.description(
    'Тест проверяет возможность перехода в категорию через главную страницу.')
@allure.link("https://petrovich.ru/", name="Главная страница магазина")
@pytest.mark.parametrize(('section', 'title'),
                         [('Стройматериалы', 'Древесно-плитные материалы'),
                          ('Инструмент', 'Ручной инструмент')],
                         ids=['Stroimateriali', 'Instrument'])
def test_select_category(browser_management, section, title):
    with allure.step('Открываем главную страницу магазина'):
        Navigation.open()

    with allure.step(f'Открываем "{section}"'):
        BasePage.search_section(section)

    with allure.step(f'Находим подраздел "{title}"'):
        CategoriesPage.search_categories(title)

    with allure.step(f'Проверяем, что открылась страница категории "{title}"'):
        information_page.verify_information_on_page(title)
