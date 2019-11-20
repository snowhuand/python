def get_number(prompt): #function definition
    user_input = int(input(prompt))
    return user_input

def get_name(prompt="Enter a name:"):
    user_input = str(input(prompt))
    return user_input

def check_calories(item1, item2):
    ITEM1_CALORIE = 50
    ITEM2_CALORIE = 100

    total_calories = item1 * ITEM1_CALORIE + item2 * ITEM2_CALORIE

    if total_calories > 500:
        return "Watch your diet!", total_calories
    elif total_calories > 300:
        return "You are at borderline.", total_calories
    else:
        return "You are very safe!", total_calories

#get_number() #function call
#get_name("Enter a kind of food:")
food1Qty = get_number("Enter how many quantity for food 1:")
food2Qty = get_number("Enter how many quantity for food 2:")
msg, calorie = check_calories(food1Qty, food2Qty)
print("Msg: {}\nCalorie: {}".format(msg, calorie))