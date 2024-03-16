import datetime
import calendar

from my_modules import find_index, test  # gives access to the function only
import sys

# import my_modules as mn # importing with alias name.


courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
# print(index)
# print(test)

print(datetime.date.today())
print(calendar.isleap(2009))
