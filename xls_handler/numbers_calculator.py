#!/usr/bin/env python3

"""Numbers calculator."""


def calculate_even_numbers(sheet, column):
    """
    Calculate how many even numbers in column.

    Args:
        sheet(openpyxl.worksheet.worksheet.Worksheet): openpyxl object.
        column(str): From this column values will be extracted.

    Returns:
        (int): Amount of even numbers.
    """
    all_column_values = list(map(lambda cell: cell.value, sheet[column]))
    even_numbers = [number for number in all_column_values[2:] if not number % 2]
    return len(even_numbers)


def calculate_prime_numbers(sheet, column):
    """
    Calculate how many prime numbers in column.

    Args:
        sheet(openpyxl.worksheet.worksheet.Worksheet): openpyxl object.
        column(str): From this column values will be extracted.

    Returns:
        (int): Amount of prime numbers.
    """
    all_column_values = list(map(lambda cell: cell.value, sheet[column]))
    prime_numbers = [number for number in all_column_values[2:] if is_prime(number)]
    return len(prime_numbers)


def calculate_less_than_point_five_numbers(sheet, column):
    """
    Calculate how many less than point five numbers in column.

    Args:
        sheet(openpyxl.worksheet.worksheet.Worksheet): openpyxl object.
        column(str): From this column values will be extracted.

    Returns:
        (int): Amount of less than point five numbers.
    """
    all_column_values = list(map(lambda cell: cell.value, sheet[column]))
    correct_numbers = convert_to_correct_format(all_column_values[2:])
    less_than_five_numbers = [number for number in correct_numbers if number < 0.5]  # Noqa: WPS459
    return len(less_than_five_numbers)


def is_prime(number):
    """
    Determine whether the number is prime.

    Args:
        number(int): Number to determine.

    Returns:
        (boolean): Is number prime.
    """
    start = int(number / 2)
    for divisor in range(start, 1, -1):
        if number % divisor == 0:
            return False
    return True


def add_zero_if_has_not(number_as_str):
    """
    Add zero at the beginning of number if it doesn't have.

    Args:
        number_as_str(str): Number to edit.

    Returns:
        (str): Number with zero at hte beginning.
    """
    return number_as_str if number_as_str.startswith('0') else '0{0}'.format(number_as_str)


def convert_to_correct_format(numbers):
    """
    Convert all strings to the correct format.

    Args:
        numbers(str): Numbers to convert.

    Returns:
        (list): Correct numbers.
    """
    without_spaces = map(lambda num_as_str: num_as_str.replace(' ', ''), numbers)
    with_dots = map(lambda num_as_str: num_as_str.replace(',', '.'), without_spaces)
    normal_numbers_as_str = map(add_zero_if_has_not, with_dots)
    return list(map(float, normal_numbers_as_str))
