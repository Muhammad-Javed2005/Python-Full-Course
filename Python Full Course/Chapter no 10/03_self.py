class Employee:
    name = "Muhammad Javed"
    language = "Urdu"  
    salary = 120000

    def getinfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


Javed = Employee() 
Javed.getinfo()
Javed.greet()


print("This program was developed by Engr. Muhammad Javed.")


