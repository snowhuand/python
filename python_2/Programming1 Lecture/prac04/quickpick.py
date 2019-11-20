import random
picks = []

userinput = int(input("How many quick picks?"))

for i in range(userinput):
    temp_picks = []
    for j in range(6):
        rand_no = random.randint(1, 45)
        while rand_no in temp_picks:
            rand_no = random.randint(1, 45)
        temp_picks.append(rand_no)
        #how to ensure no duplication?
    temp_picks.sort()
    picks.append(temp_picks)

for each in picks: #each =[5, 7, 14, 17, 39, 43]
    for inner in each: #inner = 5
        print("{:2}".format(inner), end=" ")
    print()