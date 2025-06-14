# Problem no 07:
# Write a program to print the following star pattern.


"""

  *
 ***
*****

"""

n = int(input("Enter your Number : "))

for i in range(1,n+1):
    print(" " * (n-i),end="")
    print("*"*(2*i-1),end="")
    print("\n")


print("This program was developed by Engr. Muhammad Javed.")
