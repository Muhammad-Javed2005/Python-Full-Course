# Problem no 06:
#  Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.


from random import randint

class Train:

    def __init__(slf, TrainNo):
        slf.TrainNo = TrainNo
    
    
    def book(slf, fro , to):
        print(f"Ticket  is booked in train no {slf.TrainNo} from {fro} to {to}")

    def getStatus(slf):
        print(f"Train no : {slf.TrainNo} is running on time")

    def getFare(slf, fro , to):
        print(f"Ticket  is fare in train no {slf.TrainNo} from {fro} to {to} is {randint(222,5555)}")
        

t = Train(12454)
t.book( "Karachi " , "Islamabad")
t.getStatus()
t.getFare("Karachi" , "Lahore")



print("This program was developed by Engr. Muhammad Javed.")



