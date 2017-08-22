import argparse
import re


def format_price(price):
    try:
        price = float(price)
    except (ValueError, TypeError):
        return None

    price = '{:,.2f}'.format(price).replace(',', ' ')
    if ('-' in price) or ('n' in price) or ('i' in price):
        # `-` for <0, `n` for nan,  `i` for infinity
        return None
    ending_zeros = re.search(r'[.]0+', price)
    if ending_zeros:
        price = price[:ending_zeros.start()]
    return price


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Price string formatting tool')
    parser.add_argument('price', help='Price to format')
    parameters = parser.parse_args()
    print(format_price(parameters.price))
