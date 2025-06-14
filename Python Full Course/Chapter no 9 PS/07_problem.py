# Problem no 07:
#  Write a program to find out the line number where python is present from ques 6.



with open ("log.txt") as f :
    lines = f.readlines()

word = "python"

line_no = 1

for line in lines:

    if(word in line):
        print(f"The word \"{word}\" is present in line no : {line_no}")
        break
    line_no += 1

else :
    print(f"The word \"{word}\" is not present")


print("This program was developed by Engr. Muhammad Javed.")

