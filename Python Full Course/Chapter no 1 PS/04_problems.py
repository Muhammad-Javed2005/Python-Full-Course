# Problem No 04:
# Write a python program to print the contents of a directory using os module.


import os


# Specify the directory path
directory_path = "/"


# List all files and directories
contents = os.listdir(directory_path)


# Print the contents
for item in contents:
    print(item)


print("This program was developed by Engr. Muhammad Javed.")

