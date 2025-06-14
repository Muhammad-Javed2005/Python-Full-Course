# Problem no 04:
# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.


from random import randint

class Train:

    def __init__(self, TrainNo):
        self.TrainNo = TrainNo
    
    
    def book(self, fro , to):
        print(f"Ticket  is booked in train no {self.TrainNo} from {fro} to {to}")
        pass

    def getStatus(self):
        print(f"Train no : {self.TrainNo} is running on time")
        pass

    def getFare(self, fro , to):
        print(f"Ticket  is fare in train no {self.TrainNo} from {fro} to {to} is {randint(222,5555)}")
        pass

t = Train(12454)
t.book( "Karachi " , "Lahore")
t.getStatus()
t.getFare("Karachi" , "Islamabad")


print("This program was developed by Engr. Muhammad Javed.")
