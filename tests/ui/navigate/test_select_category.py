import pytest
import allure

from models.pages.Information_page import InformationPage
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
    start = BasePage()
    information = InformationPage()
    categories = CategoriesPage()

    with allure.step('Открываем главную страницу магазина'):
        start.open_main_page()

    with allure.step(f'Открываем "{section}"'):
        start.search_section(section)

    with allure.step(f'Находим подраздел "{title}"'):
        categories.search_categories(title)

    with allure.step(f'Проверяем, что открылась страница категории "{title}"'):
        information.verify_information_on_page(title)
