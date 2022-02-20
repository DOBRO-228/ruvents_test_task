#!/usr/bin/env python3.10

""""""


def calculate_even_numbers(sheet, column):
    all_column_values = list(map(lambda cell: cell.value, sheet[column]))
    even_numbers = [number for number in all_column_values[2:] if not number % 2]
    return len(even_numbers)


def calculate_prime_numbers(sheet, column):
    all_column_values = list(map(lambda cell: cell.value, sheet[column]))
    prime_numbers = [number for number in all_column_values[2:] if is_prime(number)]
    return len(prime_numbers)


def calculate_less_than_point_five_numbers(sheet, column):
    all_column_values = list(map(lambda cell: cell.value, sheet[column]))
    normal_numbers = standardize_numbers(all_column_values[2:])
    less_than_five_numbers = [number for number in normal_numbers if number < 0.5]  # Noqa: WPS459
    return len(less_than_five_numbers)


def is_prime(number):
    start = int(number / 2)
    for divisor in range(start, 1, -1):
        if number % divisor == 0:
            return False
    return True


def add_zero_if_has_not(number):
    return number if number.startswith('0') else '0{0}'.format(number)


def standardize_numbers(numbers):
    without_spaces = map(lambda num_as_str: num_as_str.replace(' ', ''), numbers)
    with_dots = map(lambda num_as_str: num_as_str.replace(',', '.'), without_spaces)
    normal_numbers_as_str = map(add_zero_if_has_not, with_dots)
    return list(map(float, normal_numbers_as_str))
