# Problem  no 09:
# Write a program to print the following star pattern.

#           ***** 
#           *   *
#           *   *
#           *   *
#           *****


n = int(input("Enter your Number : "))

for i in range(1,n+1):
    if(i==1 or i==n):
        print("*" * n,end="")

    else:
        print("*" , end="")
        print(" " * (n-2),end="")
        print("*" , end="")
    print(" ")


print("This program was developed by Engr. Muhammad Javed.")
