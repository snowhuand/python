def add_name(name_dict):
    name = input("Enter your name:")
    dob = str(input("Enter your DOB (d/m/yyyy):")).split("/")
    name_dict[name] = dob
    return name_dict

names = {}
i = 2
while i > 0:
    i -= 1
    names = add_name(names)

for key, value in names.items():
    print("{} is {} years old.".format(key, 2016-int(value[2])))
print(names)
"""

Task today:
- Walkthrough
- Intermediate
- Do-from scratch
"""

