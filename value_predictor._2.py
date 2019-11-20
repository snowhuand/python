
from statistics import mean

def function_a():
    pass

data = [1, 1, 1, 6, 6, 6]
print (data, "please print: 1(mean), 2(value)")
x = mean(data)

options = ['1', '2']

user_input = input(">>>").lower()
while user_input not in options:
    print("Not a valid option, re-enter.")
    user_input = input(">>>").lower()
    print("Mean is :", x)

else:
    y = x - 0.05
    print("Value is :", y)

"""
while True:
    user_input = input("Enter your choice:")
    if user_input == '3':
        break # break out of while loop

    else:
        print("Error, input not accepted.")
"""
