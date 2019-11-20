# Use try except to handle problematic situation.
# Error occurs when the normal flow of program is disrupted
# ValueError occurs when the input does not tally with the expected type.
# There are 2 parts to exception: Try the risky code
#                                 Except, manage/ contain the error, could have multiple except
# When except occurs, the program will stop and look for matching except
#  When except not occuring, the program will finish the try and exit.
"""
flag = True

while(flag):
    try:
        print("1")
        user_input = int(input("Give me  number please:"))
        print("2")
        print("You have entered {}".format(user_input))
        print("3")
        flag = False
        print("4")
    except ValueError:
        print("Please enter a valid number.")
print("finish.")

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator (Enter a non zero): "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator (Enter a non zero): "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
"""
"""
1.     When will a ValueError occur? When a non-numeric is entered
2.     When will a ZeroDivisionError occur? When a zero is entered as denominator
3.   Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

"""
Get a filename from user with extension.
Try open the file using the filename.
Prompt error message if the file does not exist.
Or else, read out the content of the file.

open(), close(), try, except, print()
"""
flag = True
while(flag):
    try:
        filename = str(input("Enter a filename:"))
        if filename.isalpha():
            print("isalpha")
        filepointer = open(filename)
        for each in filepointer:
            print(each)
        filepointer.close()
        flag = False
    except FileNotFoundError:
        print("Enter a valid filename.")

