# Problem no 04:
#  A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file. 



word = "Donkey"

with open("file.txt","r") as f:
    content = f.read()

contentnew = content.replace("Donkey" , "Dog")

with open("file.txt","w") as f :
    f.write(contentnew)


print("This program was developed by Engr. Muhammad Javed.")
