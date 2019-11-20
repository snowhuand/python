"""
The following codes show how to pass data between functions and avoid
using global variables.
"""

def f1(data_list):#addition
    new_data = "abc"
    data_list.append(new_data)
    return data_list

def f2(data_list):#quit
    data_list.append("zzz")


def main():
    data = ["bbb"]
    print("I am in main()")
    print(data)
    data = f1(data) #passing of data and return store back to data.
    print(data)

    #Then pass data to f2()
    f2(data)
    print(data) #original data list is changed after f2() modifies it.

main()