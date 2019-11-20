# ItIsWell (oh my soul).txt -> It_Is_Well_(Oh_My_Soul).txt
# todo: Capitalise Oh_My_Soul
temp = "ItIsWell (oh my soul).txt"
new_str = ""

for i in range(len(temp)):
    t = temp[i] #current letter
    if i != 0 and (temp[i - 1] in "_( "):
        t= t.upper()

    if temp[i].isupper():
        if i != 0 and temp[i - 1] != "_":
            t = "_"+ t
    new_str += t
    print(new_str)

print(new_str.replace(" ", "_"))
