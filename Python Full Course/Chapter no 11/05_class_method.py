class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show() #It show the class attribute not the instance attribute because we use @class method so it will always show the class attribute 
# In class method we use cls instead of self because we are dealing with class not instance



print("This program was developed by Engr. Muhammad Javed.")
