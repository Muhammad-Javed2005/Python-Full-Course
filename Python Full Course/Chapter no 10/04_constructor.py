class Employee:
    name = "Muhammad Javed"
    language = "Urdu"  
    salary = 120000



    def __init__(self, name , languague , salary ) -> None:  #dunder method which is automatically called 
        self.name = name 
        self.language = languague
        self.salary = salary
        print("I am creating an object")

    def getinfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")



Jiya = Employee("Jiya" , "Punjabi", 15000000 )
print(Jiya.name , Jiya.language , Jiya.salary)

print("This program was developed by Engr. Muhammad Javed.")
