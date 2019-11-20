
from statistics import mean

# create a function a
def function_a():
    pass

data = [1, 1, 1, 6, 6, 6]
print (data, "please print: 1(mean), 2(value)")
x = mean(data)

# create two options for users to enter
options = ['1', '2']
user_input = input(">>>").lower()

# create a loop for the options
# usr enter "1", then the output is mean value
while user_input not in options:
    print("Not a valid option, re-enter.")
    user_input = input(">>>").lower()
    print("Mean is :", x)

# user enter "2", then the output is 3.45
else:
    y = x - 0.05
    print("Value is :", y)

# if user enter any other value, it will display invalid
"""
while True:
    user_input = input("Enter your choice:")
    if user_input == '3':
        break # break out of while loop

    else:
        print("Error, input not accepted.")
"""
