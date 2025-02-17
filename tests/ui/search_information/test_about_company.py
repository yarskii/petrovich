import allure

from models.pages.Information_page import InformationPage
from models.pages.base_page import BasePage
from models.footer import Footer
from utils.config_web import ABOUT_COMPANY_TEXT


@allure.tag('web')
@allure.feature('Информация о компании')
@allure.story('Проверка раздела "О компании"')
@allure.title('Проверка текста на странице "О компании"')
@allure.label("owner", "Ярослав Гусев")
@allure.description('Тест проверяет наличие корректного описания компании на странице "О компании".')
@allure.link("https://petrovich.ru/about/", name="Страница 'О компании'")
def test_about_company(browser_management):
    start = BasePage()
    select = Footer()
    information = InformationPage()

    with allure.step('Открываем главную страницу магазина'):
        start.open_main_page()

    with allure.step('Переходим на страницу "О компании"'):
        select.about_company()

    with allure.step('Проверяем наличие описания компании на странице'):
        information.cheking_about_company_text(ABOUT_COMPANY_TEXT)
