"""
from math import *

area = 30 * pi

print("The area is :", area)
"""
#variable type
x = 20 # The integer, whole number
y = 30.0  #float data type

z = x + y #addition
a = x - y # subtraction

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y) # integer division
print(x ** 3)
print(x % y)

# Augmented operator/ shortcut operator
x += 10 # x = x +10
print(x)
x -= 5
x *= 2
x /= 5
print(x)
# change data type to be integer
print(int(x))
print(float(x))
print(str(x))

# logical operator: and, or
if x == 10 and y == 5:
    print("true")
elif x ==10:
    print("x is 10")
else:
    print("false")

print(-x)

x = 5
while x > 0:
    x -= 1
    print(x)
print("*****************")
# range(start, end, step)
for num in range(10, 0, -2):
    print(num)

print("-------------")
# the ending number is always excluded
# the beginning number is always included
for num in range(5):
    print(num)