"""
Overview of Advanced OOP Topics
"""

# Advanced OOP topics include:
# - Multiple Inheritance
# - Mixins
# - Composition
# - Decorators and Metaclasses

class Engine:
    def start(self):
        print("Engine started")

class ElectricMotor:
    def charge(self):
        print("Charging motor")

# Multiple inheritance
class ElectricCar(Engine, ElectricMotor):
    def run(self):
        self.start()
        self.charge()
        print("Electric car is running")

car = ElectricCar()
car.run()

print("This program was developed by Engr. Muhammad Javed.")

