"""
num_list = [10, 30, 40, 70]

while True:
    num = int(input("Enter num:"))
    if num == -1:
        break
    num_list.append(num)

print(num_list)
"""
"""
Write a program that does the following:
- get symptoms from user until user enter empty string
- print High risk if the user has >= 3 symptoms
- print Risky if user has >= 1 symptom and less than 3.
- print No issue if no symptom detected.
"""

zika = ["fever", "rashes", "muscle pain", "red eyes", "headache", "joint pain"]
count = 0
while True:
    symptom = input("Enter symptom:")

    if symptom == "":
        break
    elif symptom in zika:
        count += 1
print("You've got ", count, " symptom(s).")
if count >= 3:
    print("High risk")
elif count >= 1:
    print("Risky")
else:
    print("No issue")
