#!/usr/bin/env python3

""""""


def calculate_even_numbers(numbers):
    even_numbers = [number for number in numbers if not number % 2]
    return len(even_numbers)


def is_prime(number):
    stop = int(number / 2)
    for num in range(2, stop):
        if number % num == 0:
            return False
    return True


def calculate_prime_numbers(numbers):
    prime_numbers = [number for number in numbers if is_prime(number)]
    return len(prime_numbers)


def add_zero_if_has_not(number):
    return number if number.startswith('0') else '0{0}'.format(number)


def standardize_numbers(numbers):
    without_spaces = map(lambda num_as_str: num_as_str.replace(' ', ''), numbers)
    with_dots = map(lambda num_as_str: num_as_str.replace(',', '.'), without_spaces)
    normal_numbers_as_str = map(add_zero_if_has_not, with_dots)
    return map(float, normal_numbers_as_str)


def calculate_less_than_five_numbers(numbers):
    normal_numbers = standardize_numbers(numbers)
    less_than_five_numbers = [number for number in numbers if number < 0.5]  # Noqa: WPS459
    return len(less_than_five_numbers)
