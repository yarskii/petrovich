from random import choice, randint

import requests
import logging
from models.api.cookie_manager import CookieManager
from utils.config_web import headers, url_api, params

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class ProductAPI:
    def __init__(self):
        self.cookie_manager = CookieManager()

    def send_request(self, method, url, json_data=None):
        response = requests.request(
            method,
            url,
            headers=headers,
            params=params,
            cookies=self.cookie_manager.get_browser_cookies(),
            json=json_data,
        )
        return response

    def get_product_guids_in_section(self, section):
        product_guids = []

        section_url = f'{url_api}/catalog/v5/sections/{section}/products'
        response_data = self.send_request('GET', section_url)

        assert response_data.status_code == 200

        response_json = response_data.json()

        for product in response_json['data']['products']:
            product_guids.append(product['product_guid'])

        return product_guids

    def add_product_in_cart(self, product_guids):
        for product_guid in product_guids[:2]:
            json_data = {'qty': randint(1, 10000)}
            product_url = f'{url_api}/cart/v2/products/{product_guid}'
            response_data = self.send_request('POST', product_url, json_data)

            assert response_data.status_code == 200

            response_json_product = response_data.json()
            logging.info(response_json_product['state']['title'])

    def get_sections(self):
        sections_dict = {}
        for i in range(6):
            tree_url = f'{url_api}/catalog/v5/sections/tree/{i}'
            response_data = self.send_request('GET', tree_url)
            response_json = response_data.json()

            assert response_data.status_code == 200

            stack = list(response_json['data']['sections'])

            for section in stack:
                if section['sections'] is not None:
                    section_key = f"{section['code']} {section['title']}"
                    sections_dict[section_key] = []

                    for category in section['sections']:
                        category_key = f"{category['code']}: {category['title']}"
                        sections_dict[section_key].append(category_key)

        random_section = choice(list(sections_dict.keys()))
        random_category = choice(sections_dict[random_section]).split(': ')
        logging.info(f'Выбрана категория "{" ".join(random_category)}" из секции "{random_section}"')

        return random_category
