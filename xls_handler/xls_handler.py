#!/usr/bin/env python3.10

""""""

from openpyxl import load_workbook
import argparse
import sys
from xls_handler.numbers_calculator import (
    calculate_even_numbers,
    calculate_prime_numbers,
    calculate_less_than_point_five_numbers,
)


def calculate(filepath=None):
    excel_file = load_workbook(filepath)
    sheet = excel_file['Tasks']
    sys.stdout.write('There are {0} even numbers\n'.format(calculate_even_numbers(sheet, 'B')))
    sys.stdout.write('There are {0} prime numbers\n'.format(calculate_prime_numbers(sheet, 'C')))
    sys.stdout.write(
        'There are {0} numbers which less than point five\n'.format(calculate_less_than_point_five_numbers(sheet, 'D')),
    )


def main():
    """CLI command."""
    parser = argparse.ArgumentParser(
        usage='calculate <filepath>',
        description='Do some calculations.',
        argument_default=argparse.SUPPRESS,
        add_help=False,
    )
    parser.add_argument(
        'filepath',
        help=argparse.SUPPRESS,
    )
    parser.add_argument(
        '-h',
        '--help',
        action='help',
        help='display help for command',
    )
    args = parser.parse_args()
    calculate(args.filepath)


if __name__ == '__main__':
    main()
