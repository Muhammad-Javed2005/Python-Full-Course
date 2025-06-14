# Problem no 01:
# Write a program to find the greatest of four numbers entered by the user.



a1 = int(input("Enter the number 1 : "))
a2 = int(input("Enter the number 2 : "))
a3 = int(input("Enter the number 3 : "))
a4 = int(input("Enter the number 4 : "))
a5 = int(input("Enter the number 5 : "))


if(a1>a2 and a1>a3 and a1>a4 and a1>a5):
    print(f"The greatest number is {a1}")

elif(a2>a1 and a2>a3 and a2>a4 and a2>a5):
    print(f"The greatest number is {a2}")

elif(a3>a1 and a3>a2 and a3>a4 and a3>a5):
    print(f"The greatest number is {a3}")

elif(a4>a1 and a4>a2 and a4>a2 and a4>a5):
    print(f"The greatest number is {a4}")

else:
    print(f"The greatest number is {a5}")


print("This program was developed by Engr. Muhammad Javed.")
