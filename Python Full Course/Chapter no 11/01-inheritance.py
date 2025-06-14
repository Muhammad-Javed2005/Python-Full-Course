class Employee:
    company = "ITC"
    def show(self , name , salary):
        self.name = name
        self.salary = salary
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


class Programmer:
    company = "ITC Infotech"
    def show(self , name , salary):
        self.name = name
        self.salary = salary
        print(f"The name is {self.name} and the salary is {self.salary}")

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


class Programmer(Employee):
    company = "ITC Infotech"
    language = "Python"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

print(a.company, b.company)

a.show("Javed" , 15000)
b.show("Anus" , 34000)
b.showLanguage()


print("This program was developed by Engr. Muhammad Javed.")
