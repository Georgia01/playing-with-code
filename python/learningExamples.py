
# function example asking for input. functions should be lower and use underscores
def get_name():
    return input('What is your name? ')  

name = get_name()
name2 = 'Ant'

# different ways to format print statements
print('')
print('Hello, ', name.upper(), '!')
print('Hello to ' + name2 + ' also!')
print('Hello for a third time, {}!'.format(name))

# should be able to do this but doesn't like
# print(f'Hello to {name2} again!')

# Types
print("Variable name is of type: ", type(name))

# can typecast using float(), str(), int() and bool('True')
# bool() function will always return True unless the variable is empty, 0, None or False.
# logical operators are and, or, not()

print('')
age = 4

if name.upper() == 'BOO' and age > 10:
    print('Boo who to you!')
elif age < 5:
    print('We found a toddler!')
else:
    print('Who you?')

# for loop time
nums = [4,6,2]
for num in nums:
    print(num)

print('')

for i in range(3):
    print(i)

print('')
teams = [['Jody', 'Abe'], ['Abhishek', 'Kim'], ['Taylor', 'Jen']]
for team in teams:
    for item in team:
        print(item)

# while
print('')
counter = 3
while counter > 0:
    print(counter)
    counter -= 1