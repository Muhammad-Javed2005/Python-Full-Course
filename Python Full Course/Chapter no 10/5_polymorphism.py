class Device:
    def operate(self):
        pass

class Printer(Device):
    def operate(self):
        print("Printing document...")

class Scanner(Device):
    def operate(self):
        print("Scanning document...")

class FaxMachine(Device):
    def operate(self):
        print("Sending fax...")

# Polymorphic behavior

for device in [Printer(), Scanner(), FaxMachine()]:
    device.operate()


print("This program was developed by Engr. Muhammad Javed.")

