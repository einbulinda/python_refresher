# FUNCTIONS


"""
def hello_func():
    pass  # We don't want to pass in things now and want to leave it blank.

print(hello_func())
"""


def hello_func(greeting, name='You'):
    return '{}, {}.'.format(greeting, name)


# print(hello_func('Hi', 'Corey'))

# POSITIONAL KEYWORD ARGUMENTS
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

# student_info('Math', 'Art', name='John', age=22)

# student_info(courses, info)

# student_info(*courses, **info)

# EXAMPLES OF FUNCTIONS

# Number of days per month, first value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Returns True for leap years and False for non-leap years"""  # Doc string helps define what a function does.
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Returns number of days in that month in that year"""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(days_in_month(2025, 2))
