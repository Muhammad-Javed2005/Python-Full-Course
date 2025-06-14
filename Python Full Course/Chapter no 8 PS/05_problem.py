# Problem no 05:
# Write a python function to print first n lines of the following pattern:
#       ***
#       **
#       *


def pattern(n):
    if (n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(3)


print("This program was developed by Engr. Muhammad Javed.")
