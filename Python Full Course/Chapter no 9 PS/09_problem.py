# Problem no 09:

# Write a program to find out whether a file is identical & matches the content of another file.


with open ("file1.txt") as f:
    content1 = f.read()

with open ("file2.txt") as f:
    content2 = f.read()


if (content1 == content2):
    print("Both files are identical")

else:
    print("Both files are not identical")


print("This program was developed by Engr. Muhammad Javed.")
