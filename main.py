"""

"""
student = {'name': "Einstein", 'age': 33, 'courses': ['Python', 'TADAT']}

# print(student['courses'])

# Using get method
print(student.get('phone', 'Not Found'))  # Does not throw error but none or defined string

# Updating values
student.update({'name': 'Bulinda', 'phone': '0702688826'})

# Delete
# del student['age']
age = student.pop('age')

# Looping
print(student.keys())
print(student.items())

for key, value in student.items():
    print(key, value)
