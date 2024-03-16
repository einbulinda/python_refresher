nums = [1, 2, 3, 4, 5]

'''
for num in nums:
    if num == 3:
        print('Found 3')
        break
    print(num)
'''
"""for num in nums:
    if num == 3:
        print('Found 3')
        continue
    print(num)"""

# Break & Continue

# Loop within a Loop

'''for num in nums:
    for letter in 'abc':
        print(num, letter)'''

# Avoid nested loops
# Another way to loop is by range kw

'''for i in range(1, 10):
    print(i)'''

# While loop - runs until condition evaluates to false

x = 0
'''while x < 10:
    if x == 5:
        break
    print(x)
    x += 1'''

# indefinite loop until value is found
while True:
    if x == 5:
        break
    print(x)
    x += 1

