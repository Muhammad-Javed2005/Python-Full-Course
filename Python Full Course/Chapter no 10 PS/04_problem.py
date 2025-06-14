# Problem no 04:
# Add a static method in problem 2, to greet the user with hello


class Calculator:
    def __init__(self,n):
        self.n = n 
    
    def square(self):
        print(f"The square  is  {self.n*self.n}")

    def cube(self):
        print(f"The cube  is  {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The square root   is  {self.n**1/2}")

    @staticmethod
    def good():
        print("Hello ! How are you")

a = Calculator(16)
a.square()
a.cube()
a.squareroot()
a.good()


print("This program was developed by Engr. Muhammad Javed.")
