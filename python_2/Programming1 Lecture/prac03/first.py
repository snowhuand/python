user_input = input("Enter your name:")
while user_input == "":
    user_input = input("Enter your name:")

print(user_input[::2])