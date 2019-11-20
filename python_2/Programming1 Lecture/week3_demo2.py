

"""
Functions:
1. name **- meaningful, lowercase
2. input arguments- optional, can be up to any number
3. return- optional,usually only one
"""

def function_name():
    pass

def file_reading(filename):
    filepointer = open(filename)
    for each in filepointer:
        print(each)
    filepointer.close()


def main():
    flag = True
    while (flag):
        try:
            filename = str(input("Enter a filename:"))
            file_reading(filename)
            flag = False
        except FileNotFoundError:
            print("Enter a valid filename.")

main()

