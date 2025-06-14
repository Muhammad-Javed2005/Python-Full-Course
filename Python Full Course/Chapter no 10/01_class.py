class Employee:
    name = "Muhammad Javed"
    language = "Urdu"  # This is a class attribute 
    salary = 120000

Javed = Employee()
Javed.name = "Muhammad Javed Aftab"  # This is a object/ instance  attribute
print(Javed.name , Javed.language , Javed.salary)

Jiya = Employee()
Jiya.name = "Jiya"
print(Jiya.name , Jiya.language , Jiya.salary)

# Here name is object/instance attribute and salary and language are class attribute as they direactly belong 
# to the class. 

print("This program was developed by Engr. Muhammad Javed.")


