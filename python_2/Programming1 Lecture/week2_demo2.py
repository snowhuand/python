"""
String methods (functions)

"""
str1 = "howdy today."
print(str1.capitalize())
print(str1.upper())
print(str1) # Immutable string
#str1[1] = 'h' #immutablr
print(str1.isupper())
print(len(str1))

for index, letter in enumerate(str1):
    print(index, "-> ", letter)

print("to" in str1)

# string format
greet = "How are you?"
name = "John"
day = "Monday"
new_str = "{0} {1}. \nGood {2}, {1}!".format(greet, name, day)
print(new_str)

short_str = "This"
print("{:20s} is CP1404.".format(short_str)) #default alignment of string is left
print("{:>20s} is cp1404.".format(short_str)) #align to right
print("{:^20s} is cp1404.".format(short_str)) #align centre

number1 = 523
print("${}".format(number1))
print("${:.2f}".format(number1))
print("${:010.2f}".format(number1)) #zero padding.
