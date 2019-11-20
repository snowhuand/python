"""
Write a code snippets to count the number of times the word occurs in a list.
Given:
words = ['John', 'Jane', 'John']
hint: Use dictionary and try/except
"""

words = ['John', 'Jane', 'John']
counts_dict = {} # {"John": 2, "Jane": 1}
for word in words:
    try:
        counts_dict[word] += 1
    except KeyError:
        counts_dict[word] = 1
    print(counts_dict)

x = 10
y = 9.9
z = "abc"
w = [x, y, z, x]
print(type(x))
print(type(y))
print(type(z))
print(type(w))

# polymorphism= many forms
# eg. len() method that calculates the size of a data
# can be applied to str and list
print(len(z))
print(len(w))

from week7_class2 import Hero
captain_america = Hero("captain")
