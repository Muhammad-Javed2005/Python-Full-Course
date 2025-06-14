# Problem no 11:
# Write a python program to rename a file to “renamed_by_ python.txt.

with open ("original_file.txt", "r") as f:
    data = f.read()


with open ("renamed_by_ python.txt", "w") as f:
    f.write(data)


print("This program was developed by Engr. Muhammad Javed.")

