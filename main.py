
# Lists Tuples & Sets

courses = ['History', 'Physics', 'Math', 'CompSci']
# courses_2 = ['Art', 'Education']
nums = [1, 5, 8, 6, 9]

# courses.append(courses_2)  # Will add the actual list as a member @ end.

# courses.insert(2, "Mathematics") # Takes 2 values, (index, item to add)

# courses.extend(courses_2) # adds individual courses 2 values.

# Removing values

# courses.remove('Math')
# popped = courses.pop()

# courses.reverse()
# courses.sort(reverse=True)
sorted_courses = sorted(courses)  # Sorted version of list. No altering of original.

# Find index of CompSci
# print(courses.index('CompSci'))

# Check if item is in list
# print('Art' in courses)

'''
for index, course in enumerate(courses, start=1):
    print(index, course)
'''
# Turn list in comma separated string
course_str = ', '.join(courses)

# String into list
new_list = course_str.split(', ')


"""
TUPLES
lists are mutable, tuples are immutable
tuples are used for list of values that you dont intent to change
We use brackets instead of square brackets
No appending, removing, adding to tuples
"""

"""
SETS
Unordered values
orders change on execution
They remove duplicates on execution
created with curly brackets
They are optimized for membership tests
intersection method - item in both sets
difference method - not in both
union method - combine sets.

"""

cs_courses = {'History', 'Math', 'Physics', 'Math'}

print('Math' in cs_courses)  # membership test

# Creating empty lists, sets and tuples

# Empty List
empty_list = []
empty_list_2 = list()

# Empty Tuple
empty_tuple = ()
empty_tuple_2 = tuple()

# Empty Set
empty_set = set()
not_empty_set = {}  # This will create a dict

