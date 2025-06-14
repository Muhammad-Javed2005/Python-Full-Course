# Problem no 02:
# Write a python program using function to convert Celsius to Fahrenheit.


def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter your temp in fahrenheit : " ))
c = f_to_c(f)
c = round(c,3)
print(f"The temp of {f}°F is equal to {c}°C ")


print("This program was developed by Engr. Muhammad Javed.")

