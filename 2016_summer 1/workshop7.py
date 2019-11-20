#class variable
number = 0#int()#function to convert something into integer
def getValue():
    number = int(input("Enter a value"))
    print(number)
def main():
    print(number)
def process_string():
    string_1 = "Hello world!"
    #index no= "0123456789
    print("The whole string: ", string_1)
    print("The first letter: ", string_1[0])
    print("The last letter: ", string_1[-1])
    print("Slicing from left: ", string_1[:3])
    print("Slicing from middle: ", string_1[1:4]) #index 1, 2, 3
def split_string():
    print("*" * 20)
    str_1 = "A stitch in time saves nine"
    half = int(len(str_1)/2)
    print(str_1[:half]) #index 0, 1, 2, 3,...12
    print(str_1[half:]) #index 13, 14, 15....26
    print("*" * 20)
split_string()
"""
Today task: Task 3, 4, 5
"""
