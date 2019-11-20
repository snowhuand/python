"""
Write a function that takes in a number (0 to 6)  as input argument the return the corresponding day of the week.
eg. get_day(0) should return "Sun"
"""
import random
from operator import itemgetter

def get_day(num):
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    return days[num]

foods = ['Sandwich', 'Burger', 'Chicken Rice', 'Udon', 'Teriyaki chicken', 'Sushi', 'Fried Noodles']
#print(list(range(7)))
for i in range(7): #7 days in a week
    daily_meals = []
    for j in range(3): #3 meals
        rand_num = random.randint(0,len(foods)-1)
        daily_meals.append(foods[rand_num])
    print("{}: breakfast {}; lunch {}; dinner {}. ".format(get_day(i), daily_meals[0], daily_meals[1], daily_meals[2]))

name_list = [["John", 20, "yellow"], ["Jordan", 25, "red"], ["Dunken", 25, "Black"]]
print("before sort: ", foods)
foods.sort()
print("after sort: ", foods)
print("before sort: ", name_list)
name_list.sort(key=itemgetter(1, 0))
print("after sort: ", name_list)

def test(num1=0, num2=0, text1=""):
    print(num2)
    return 3, 5

test(num1=99)

print(foods)

str1 = "**"
str2 = "nfjhace"
print(str1.join(foods))
print(str2)
print(sorted(str2))

print(list(tuple(foods)))

new_list = []
for each in range(100):
    new_list.append(each * 2)

new_list_comp = [each**2 for each in range(100)]
print(new_list_comp)




