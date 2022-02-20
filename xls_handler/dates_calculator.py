#!/usr/bin/env python3

""""""

import calendar
import re

from dateutil import parser


def calculate_tuesdays(sheet, column):
    all_column_values = list(map(lambda cell: cell.value, sheet[column]))
    values_without_rus_letters = [re.sub('[А-я]', '', cell_value) for cell_value in all_column_values[2:]]
    weekdays = [parser.parse(date).weekday() for date in values_without_rus_letters]
    tuesdays = [weekday for weekday in weekdays if weekday == 2]
    return len(tuesdays)


def calculate_last_tuesdays(sheet, column):
    all_column_values = list(map(lambda cell: cell.value, sheet[column]))
    dates = [parser.parse(date) for date in all_column_values[2:]]
    last_tuesdays = [date for date in dates if is_last_weekday_of_month(date)]
    return len(last_tuesdays)


def is_last_weekday_of_month(date):
    month = calendar.monthcalendar(date.year, date.month)
    penultimate_sundays = month[-2][calendar.TUESDAY]
    last_sundays = month[-1][calendar.TUESDAY]
    last_weekday = max(penultimate_sundays, last_sundays)
    return date.day == last_weekday
