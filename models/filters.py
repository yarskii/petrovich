from selene import browser, be, have
import logging

logging.basicConfig(level=logging.INFO)


class PriceFilter:

    def format_price(self, value):
        if len(value) > 3:
            return f'{value[:-3]}\u2009{value[-3:]}'
        return value

    def set_min_price(self, min_price):
        browser.element('input[name="min"]').should(be.visible).type(min_price)

    def set_max_price(self, max_price):
        browser.element('input[name="max"]').should(be.visible).type(max_price)

    def checking_price_filter(self, min_price, max_price):
        formatted_min = self.format_price(min_price)
        formatted_max = self.format_price(max_price)

        price = browser.element('.product-list-filter-container').should(be.visible)
        price.should(have.text(f'Цена, руб: от {formatted_min} до {formatted_max}'))

        logging.info(f'Проверка прошла успешно!')
