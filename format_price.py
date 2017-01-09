from argparse import ArgumentParser
from textwrap import wrap


def format_price(price):
    try:
        inverse = str(int(float(price)))[::-1]
        return ' '.join(wrap(inverse, 3))[::-1]
    except ValueError:
        return 'NaN'


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('price')
    print(format_price(parser.parse_args().price))
