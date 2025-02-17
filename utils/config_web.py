from dotenv import load_dotenv
import os

load_dotenv()

url_api = os.getenv('URL_API')
user_name = os.getenv('EMAIL')
user_password = os.getenv('PASSWORD')

json_data = {
    'password': user_password,
    'email': user_name
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json',
    'Referer': 'https://petrovich.ru/',
}

params = {'city_code': 'spb'}

ABOUT_COMPANY_TEXT = (
    'Строительный торговый дом «Петрович» — отечественная компания, '
    'которая специализируется на продаже строительных и отделочных материалов, '
    'а также комплектации крупных объектов жилой, коммерческой и социальной инфраструктуры. '
    'Основана в 1995 году в Санкт-Петербурге.'
)
