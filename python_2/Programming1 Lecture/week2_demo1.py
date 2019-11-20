# String

# String can be declared using ' '
username = 'John'
print("My name is ", username)

fullname = "John Han"
print("Full name is " + fullname)

long_str = """
Line 1
     Line 2
Line 3
"""
print(long_str)

# print timetable
print("My timetable.")
for each in range(10):
    print(each, " * 5 = ", each * 5)

# escape character
# \n New line; \t a tab space; \'; \"
print("\t1 * 1 = 1  \n\t1 * 2 = \'2")

# ascii printing
print(chr(97)) #Print the ascii character associated with ordinal number 97
print(ord('a'))
"""
for num in range(32, 117):
    print(str(num), "->", chr(num), end="******")
"""
greet = "How are you?"
name = "John"
day = "Monday"

print("Original str: ", greet)
print("Position 1:", greet[1])
print("Position 0-3:", greet[0:4]) #slicing
print("Position at odd number: ", greet[1::2]) #print starting from position 1 to the end, separated by 2 position
print("Negative indexing -2: ", greet[-2])
print("In between 2, -2", greet[2:-1])
# String slicing [start:end:step]
"""
Given the string str1 = "abcdefghij", write code that will produce the following:
a) 'jihgfedcba'
b) 'adgj'
c) 'igeca'
"""
str1 = "abcdefghij"
print(str1[-1::-1])
print(str1[::3])
print(str1[-2::-2])
