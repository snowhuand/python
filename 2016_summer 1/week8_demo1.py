# declare the options available for menu

def function_a():
    pass

options = ['a', 'b', 'c']

#print('g' in options)

user_input = input(">>>").lower()

while user_input not in options:
    print("Not a valid option, re-enter.")
    user_input = input(">>>").lower()

print("Good bye~!")
"""
while True:
    user_input = input("Enter your choice:")
    if user_input == 'q':
        break # break out of while loop
    elif user_input == 'a':
        function_a()
    else:
        print("Error, input not accepted.")
"""

