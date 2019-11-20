import random

def compute(num1, num2):
    print("Num1: ", num1, "; Num2: ", num2)
    print("Addition:", (num1 + num2))
    print("Subtraction: ", (num1 - num2))
    print("Multiplication: ", (num1 * num2))
    print("Division: ", (num1 / num2))
    print("Modulus: ", (num1 % num2))
    print("Power: ", (num1 ** num2))
    print("Integer division:", (num1 // num2))

def get_lucky_num():
    rand_num = random.randint(1,100)
    return rand_num
    #print(rand_num)

#compute(15, 10)
# compute(12, 34)

# 1 store return value in variable
ret_value = get_lucky_num()
print(ret_value)

# 2 Use the return value directly
ret_value2 = get_lucky_num()
print(get_lucky_num())

compute(ret_value *10, ret_value2+20)



# Function can have any number of input parameters
# But it usually only have 1 return value

"""
Go to "github.com"
"Sign up" a new account
MUST use your jcu email address
Go to "https://education.github.com/"
Click "Get the pack"
Then click "Request a discount"


"""