import os
import shutil
import os.path

#print(os.getcwd())
#target_path = "/Users/yen/Dropbox/temp/"
#os.chdir(target_path)
#print(os.getcwd())
#print(os.listdir("."))
#for names, dirs, files in os.walk("."):
#    print(names, dirs, files)
"""
Activity
--------
I. Explore the current directory, if it is a python file, print out the name only without extention.
II. Create a py folder and copy all python file into the py folder.
hint: import os, os.path
      os.listdir(path)-> list
      for loop loop through the list
      check the filename contains .py

"""
curr_dir = os.getcwd()
to_dir = os.path.join(curr_dir, "py")

os.mkdir(to_dir)

for each_file in os.listdir(curr_dir):
    if os.path.isfile(each_file):
        file_list = each_file.split(".")
        if file_list[1] == "py":
            print(file_list[0])
            print(curr_dir)
            print(to_dir)
            from_file = os.path.join(curr_dir, each_file)
            to_file = os.path.join(to_dir, each_file)
            shutil.copyfile(from_file, to_file)


"""
Programming Languages:
Python, Java, C, C++, Ruby, C#, Javascript, R, Perl, PHP, CGI, VB, Pascal, VHDL,  Small talk.Eiffel, Go
"""