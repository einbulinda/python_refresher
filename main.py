# Strings
name = 'Jennifer'
# print(name[1:-1])  # square notation for strings.

# Formatted Strings
first = 'Einstein'
last = 'Bulinda'
message = f"{first} [{last}] is a coder."  # Formatted String.
# print(message)

course = "Python for beginners"

# print(len(course))

# We can use len() to enforce a limit to user input.
# Can be used to count the number of items in a list.

# A method is a function that belongs to a specific object.

# print(course.upper())  # Does not modify the original string.

print(course.find('beginners'))  # It is case-sensitive.

print(course.replace('beginners', 'Absolute Beginners'))

# In Operator
print('Python' in course)  # Returns a boolean value


