"""
Write a function that takes an integer and prints the numbers from that down to 0.
Hint: while or for or recursion
eg. print_num(5)
output:
5
4
3
2
1
0
"""

def print_num_recursion(x):
    print(x)
    if x == 0:
        return
    else:
        print_num_recursion(x-1)

def print_num_while(x):
    while x >= 0:
        print(x)
        x -= 1

def print_num_for(x):
    for i in range(x, -1, -1):
        print(i)

#print_num_recursion(7)

def recurse(n): #1) n=4 4) n=3
    if n <= 0:
        print("Thing!") # Thing
    else:
        print(n) #2) 4 5) 3, 2, 1
        recurse(n - 1) #3) recurse(3) 6)recurse(2)
        print(n)

recurse(4)

