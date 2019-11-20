"""
TDD- test driven development
"""
#step 2: remove the error
def get_vowels(test_string): #test_string = "Hello"
    """
    This function returns the list of vowels
    :param test_string: input string
    :return: list of vowels
    >>> get_vowels("Hello")
    ['e', 'o']
    >>> get_vowels("Rain")
    ['a', 'i']
    """
    vowels = []
    for letter in test_string:
        if letter in "aeiouAEIOU":
            vowels.append(letter)
    return vowels

#start with testing the code, put in the code how it should run first
#eg. I need a function that helps me to identify the vowels in a string
# step 1
#print(get_vowels("Hello")) #['e', 'o']

import doctest
doctest.testmod()

# def sqrt(x):
#     return x ** 2
#
# #print(sqrt(4))
# #sqrt(4) => 16
# assert sqrt(4) == 16 # Insert assert with the results it is supposed to provide
# assert sqrt(2) == 4, "This doesn't work"
#
# def get_value():
#     x = int(input("Enter a positive number:"))
#     assert x > 0, "Number must be positive."
#     return x
#
# print(get_value())
