# Problem no 06:
# Write a program to calculate the factorial of a given number using for loop.


n = int(input("Enter your Number : "))
i = 1
multiple = 1

while(i<=(n-1)):
    i += 1
    multiple *= i

print(multiple)

product = 1

for i in range(1,n+1):
    product = product*i

print(f"The factroial of {n} is {product}")
print(f"The factroial of {n} is {multiple}")


print("This program was developed by Engr. Muhammad Javed.")


