"""
Introduction to OOP in Python
"""

# OOP stands for Object-Oriented Programming
# It is a paradigm based on the concept of "objects"
# Python supports OOP fully through classes and objects

print("Object-Oriented Programming (OOP) is a method of structuring a program by bundling related properties and behaviors into individual objects.")

# Medium-level Example:
# Car class banai gayi hai jisme brand aur model properties hain
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

# Object banaya gaya Car class ka
my_car = Car("Toyota", "Corolla")
my_car.display_info()


print("This program was developed by Engr. Muhammad Javed.")
