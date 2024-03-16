"""
if it's hot
    It's a hot day
    Drink plenty of water
otherwise if it's cold
    It's a cold day
    Wear warm clothes
otherwise
    It's a lovely day.
"""
'''
is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day.")

'''

# Exercise
'''
Price of a house is 1M
If a buyer has good credit,
    they need to put down 10%
Otherwise
    They need to put down 20%
Print the down payment'''

has_good_credit = False
price = 1_000_000

if has_good_credit:
    print(f"Down payment: Ksh. {price * 0.1}")
else:
    print(f"Down payment: Ksh. {price * 0.2}")


# Keys
# equal to ==
# not equal !=
# object identity  is
# and, or, not

a = [1, 2, 3]
b = [1, 2, 3]

# print(a is b)  # checks object identity.
