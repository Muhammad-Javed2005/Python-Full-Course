# Problem no 02:

# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals:
    pass 

class Pets(Animals):
    pass 

class Dog(Pets):

    @staticmethod
    def bark():
        print("Bow Bow!")


d = Dog()

d.bark()


print("This program was developed by Engr. Muhammad Javed.")
