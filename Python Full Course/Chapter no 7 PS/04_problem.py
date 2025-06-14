# Problem no 04:
# Write a program to find whether a given number is prime or not.



n = int(input("Enter your number: "))

for i in range(2,n):
    if(n%i) == 0 :
        print(f"{n} is not prime number")
        break

else:
    print(f"{n} is a prime number")


print("This program was developed by Engr. Muhammad Javed.")
