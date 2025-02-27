import json

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

current_dir = os.path.dirname(os.path.abspath(__file__))
texts_path = os.path.join(current_dir, 'texts.json')

with open(texts_path, 'r', encoding='utf-8') as file:
    texts = json.load(file)

ABOUT_COMPANY_TEXT = ' '.join(texts['about_company_text'])
