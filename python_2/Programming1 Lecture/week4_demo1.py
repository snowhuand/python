#names = []
names = ["Alice", "Tom", "John"] #list of string
ages = [10, 40, 25] #list of int

print(names[1]) #print second data
print(names[-1])

# while True:
#     name = input("Enter a name:")
#     if name == "":
#         break #exit while loop
#     names.append(name)
print(len(names))

"""
List is
- mutable (any changes, reflects on the original list), string is immutable.
- ordered (0, 1, 2, 3)
- names = ["Alice", "Tom", "John"]
- names[0:1] :slicing
- names + names :concatenation
- names * 10: repeat
- if "john" in names: check if it's inside the list
- len : get the total length
"""
