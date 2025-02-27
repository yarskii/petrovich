import allure

from models.navigation import Navigation
from models.pages.Information_page import information_page
from models.footer import Footer


@allure.tag('web')
@allure.feature('Информация о компании')
@allure.story('Проверка раздела "О компании"')
@allure.title('Проверка текста на странице "О компании"')
@allure.label("owner", "Ярослав Гусев")
@allure.description('Тест проверяет наличие корректного описания компании на странице "О компании".')
@allure.link("https://petrovich.ru/about/", name="Страница 'О компании'")
def test_about_company(browser_management):
    with allure.step('Открываем главную страницу магазина'):
        Navigation.open()

    with allure.step('Переходим на страницу "О компании"'):
        Footer.about_company()

    with allure.step('Проверяем наличие описания компании на странице'):
        information_page.cheking_about_company_text()
