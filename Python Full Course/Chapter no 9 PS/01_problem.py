# Problem no 01:
#  Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.



f = open("poem.txt")
content = f.read()

if("Twinkle" in content):
    print("This poem is a Twinkle, twinkle, little star!")

else:
    print("This poem is not a  Twinkle, twinkle, little star!")

print("Thanks You for contact Muhammad Javed")
    

print("This program was developed by Engr. Muhammad Javed.")
