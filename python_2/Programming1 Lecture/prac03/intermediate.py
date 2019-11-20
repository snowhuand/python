def get_number(lower, upper):
    while (True):
        try:
            user_input = int(input("Enter a number ({}-{}):".format(lower, upper)))
            if user_input < lower:
                print("Number too low.")
            elif user_input > upper:
                print("Number too large.")
            else:
                return user_input
        except ValueError:
            print("Error in number")


return_value = get_number(10, 50)
print("The returned value is {}".format(return_value))
