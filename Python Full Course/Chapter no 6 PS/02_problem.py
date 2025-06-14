# Problem no 02 :
#  Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. 
# Assume 3 subjects and take marks as an input from the user.



mark1 = int(input("Enter the mark of English : "))
mark2 = int(input("Enter the mark of Math : "))
mark3 = int(input("Enter the mark of Physics : "))

name = input("Enter your name : ")

total_percentage = (100*((mark1+mark2+mark3)/300))

if(total_percentage>=40 and mark1>33 and mark2>33 and mark3>33):
    print(f"Congratulation {name} ! , You are pass,Your percentage is {total_percentage}")
    print("Kindly give me a box of sweets as soon as possible.")

else:
    print(f"Alas {name}!, You are fail,Your percentage is {total_percentage}")
    print("If you want to pass this year, then give me 1000 dollars urgently.")

print("Thanks you to connect me MUHAMMAD JAVED")


print("This program was developed by Engr. Muhammad Javed.")
