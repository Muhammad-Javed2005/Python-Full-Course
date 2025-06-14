# Problem no 06:
#  Write a program to mine a log file and find out whether it contains ‘python’.



with open ("log.txt") as f :
    content = f.read()

word = "python"

if(word in content):
    print(f"The word \"{word}\" is present")

else :
    print(f"The word \"{word}\" is not present")


print("This program was developed by Engr. Muhammad Javed.")

