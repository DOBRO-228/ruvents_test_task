#!/usr/bin/env python3

"""Dates calculator."""

import calendar
import re

from dateutil import parser


def calculate_tuesdays(sheet, column):
    """
    Calculate how many tuesdays in column.

    Args:
        sheet(openpyxl.worksheet.worksheet.Worksheet): openpyxl object.
        column(str): From this column values will be extracted.

    Returns:
        (int): Amount of tuesdays.
    """
    all_column_values = list(map(lambda cell: cell.value, sheet[column]))
    values_without_rus_letters = [re.sub('[А-я]', '', cell_value) for cell_value in all_column_values[2:]]
    weekdays = [parser.parse(date).weekday() for date in values_without_rus_letters]
    tuesdays = [weekday for weekday in weekdays if weekday == 2]
    return len(tuesdays)


def calculate_last_tuesdays(sheet, column):
    """
    Calculate how many last tuesdays of the month in column.

    Args:
        sheet(openpyxl.worksheet.worksheet.Worksheet): openpyxl object.
        column(str): From this column values will be extracted.

    Returns:
        (int): Amount of last tuesdays.
    """
    all_column_values = list(map(lambda cell: cell.value, sheet[column]))
    dates = [parser.parse(date) for date in all_column_values[2:]]
    last_tuesdays = [date for date in dates if is_last_tuesday_of_month(date)]
    return len(last_tuesdays)


def is_last_tuesday_of_month(date):
    """
    Determine whether the date is the last tuesday of the month.

    Args:
        date(datetime.datetime): Python datetime object.

    Returns:
        (boolean): Is date the last sunday.
    """
    month = calendar.monthcalendar(date.year, date.month)
    penultimate_tuesday = month[-2][calendar.TUESDAY]
    last_tuesday = month[-1][calendar.TUESDAY]
    last_tuesday = max(penultimate_tuesday, last_tuesday)
    return date.day == last_tuesday
