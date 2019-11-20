"""
# File IO method 1
output_file = open("output.txt", "w")
output_file.write("Line1...\n")
output_file.write("Line2...\n")
output_file.close()

#File IO method 2 *****
output_file2 = open("output2.txt", "w")
print("statement 1", file=output_file2)
print("statement 2", file=output_file2)
output_file2.close()"""

input_file = open("output.txt", "r")
for line in input_file:
    #line = Data1, Data2, Data
    data = line.split(",")
    # data[0] = Data1
    # data[1] = Data2
    # data[2] = Data3
    for each in data:
        print(each)
    #print(line, end="")
input_file.close()
