"""
Get score from user
Display the corresponding grade

"""

def get_grade(score):
    grade = ""
    if score >= 85:
        grade = "HD"
    elif score >= 75:
        grade = "D"
    elif score >= 65:
        grade = "C"
    elif score >= 50:
        grade = "P"
    else:
        grade = "N"
    return grade

def print_stars(num):
    for i in range(0, num, 1): #0, 1, 2, 3, ...num-1
        print("*" * i) #+, -, *, /, //, %, **

def print_while(num):
    # Conver print_stars(num) to be using while instead of for
    # Group activity
    i = 0
    while i <= num:
        print("*" * i)
        i += 1 #exit condition, i = i + 1
        # += augmented operator
        # -= eg. i -= 3
        # *=
        # /=

def main():
 #   score = int(input("Enter your score:"))#score 60
 #   grade = get_grade(score)#get_grade(60)
 #    print("Your grade is :", grade)

 #   user_input = int(input("How many stars do you want?"))
#    print_stars(user_input)
#    print_while(user_input)

    for i in range(5):
        print(i)
    for j in range(0,5):
        print(j)
    for k in range(0,5, 1):
        print(k)

main() #running the main program
