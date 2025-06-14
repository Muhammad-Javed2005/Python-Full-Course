# Problem no 01:
#  Write a program to print multiplication table of a given number using for loop.


n = int(input("Enter your number : "))

# For Loop 

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")

# While Loop


i = 1

while(i<11):
    print(f"{n} X {i} = {n*i}")
    i += 1


print("This program was developed by Engr. Muhammad Javed.")
