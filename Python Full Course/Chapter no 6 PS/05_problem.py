# Problem no 05:
#  Write a program which finds out whether a given name is present in a list or not.



names = ["Javed","Jiya","Fiza","Mehwish","Nabila","Rida","Anas"]

name = input("Enter Your name: ").capitalize()

if(name in names):
    print(f"{name}!, You are slected")

else:
    print(f"{name}!,You are rejected")


print("This program was developed by Engr. Muhammad Javed.")
