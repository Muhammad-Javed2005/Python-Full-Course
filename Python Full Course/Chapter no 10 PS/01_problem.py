# Problem no 01:
# Create a class “Programmer” for storing information of few programmers 
# working at Microsoft.



class Programmer:
    company = "Microsoft"

    def __init__(self , name , nationality , religion , salary , language):
        self.name = name 
        self.nationality = nationality
        self.religion = religion
        self.salary = salary
        self.language = language


print("Firts Person Detials: ")
p = Programmer("Muhammad Javed" , "Non pakistani" , "Islam" , 1500000 , "Urdu")
print(f"{p.name} \n{p.nationality} \n{p.religion} \n{p.salary} \n{p. language} \n{p.company}")

print("Second Person Detail:")
p2 = Programmer("Jiya " , "Non pakistani" , "Islam" , 1300000 , "Urdu")
print(f"{p2.name} \n{p2.nationality} \n{p2.religion} \n{p2.salary} \n{p2. language}  \n{p2.company}")


print("This program was developed by Engr. Muhammad Javed.")
