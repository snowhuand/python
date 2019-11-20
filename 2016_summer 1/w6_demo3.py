import random

##### While example
userinput = input("Enter a value:")

while(userinput != "q"):
    print("value is : ", userinput.upper())
    userinput = input("Enter a value:")

##### if example
hidden_answer = random.randint(1, 5)
if (hidden_answer == 4):
    print("Bingo")
elif (hidden_answer == 3):
    print("It's three.")
else:
    print("Not bingo")

#### Todo:
# 1. Install git
# 2. Go to "Assessment" -> "CP1401 Wiki" -> "Week 6 activity"
# 3. Work on 1 task out of the 4.