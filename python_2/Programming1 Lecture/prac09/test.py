#ItIsWell (oh my soul).txt -> It_Is_Well_(Oh_My_Soul).txt
# todo: Capitalise Oh_My_Soul
temp = "ItIsWell (oh my soul).txt"
new_str = ""
new_list = []

for i in range(len(temp)):
    if temp[i].isupper():
        if i != 0 and temp[i-1] != "_":
            str_new = "_"+temp[i]

            new_list.append(str_new)
        else:
            new_list.append(temp[i])
    else:
        new_list.append(temp[i])

new_string = ""
for each in new_list:
 #   if each == " ":
  #      each = "_"
    new_string += each.replace(" ", "_")
print(new_string)

import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)