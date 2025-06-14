# Problem no 06:
# Write a program to calculate the grade of a student from his marks from the 
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F



mark1 = int(input("Enter the mark of English : "))
mark2 = int(input("Enter the mark of Math : "))
mark3 = int(input("Enter the mark of Physics : "))

name = input("Enter your name : ")

total_percentage = (100*((mark1+mark2+mark3)/300))


if(total_percentage>90):
    print(f"{name} are pass with Ex, You percentage is {round(total_percentage, 3)}")

elif(total_percentage>80 and total_percentage<=90):
    print(f"{name} are pass with A, You percentage is {round(total_percentage, 3)}")

elif(total_percentage>70 and total_percentage<=80):
    print(f"{name} are pass with B, You percentage is {round(total_percentage, 3)}")

elif(total_percentage>60 and total_percentage<=70):
    print(f"{name} are pass with C, You percentage is {round(total_percentage, 3)}")

elif(total_percentage>50 and total_percentage<=60):
    print(f"{name} are pass with D, You percentage is {round(total_percentage, 3)}")

elif(total_percentage>40 and total_percentage<=50):
    print(f"{name} are pass with E, You percentage is {round(total_percentage, 3)}")

else:
    print(f"{name} are Fail, your grade is F,You percentage is {round(total_percentage, 3)}")

print("This program was developed by Engr. Muhammad Javed.")
