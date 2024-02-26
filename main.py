# Type Conversion
"""
birth_year = input("Birth Year: ")  # What we receive from terminal is always a string.
print(type(birth_year))
age = 2024 - int(birth_year)
print(type(age))
print(age)
"""

# Exercise
weight_in_pounds = input("What is your weight in pounds? ")
conversion_rate = 0.453592
weight_in_kilos = float(weight_in_pounds) * conversion_rate
print(weight_in_kilos)
