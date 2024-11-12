# write a class train which has methods to book a ticket, get status (no of seats) and det fare information of train running under Indian Railways.

from random import randint

class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self,fromWhere,whereTo):
        self.fromWhere = fromWhere
        self.whereTo = whereTo
        print(f"Ticket is booked in train no: {self.trainNo} from {self.fromWhere} to {self.whereTo} ")

    def getStatus(self):
        print(f" Train no: {self.trainNo} is running on time")
    
    def getFare(self,fromWhere,whereTo):
        print(f"Ticket fare in train no: {self.trainNo} from {fromWhere} to {whereTo} is {randint(222,5555)}")

train = Train(123999)
train.book("Karachi","Islamabad")
train.getStatus()
train.getFare("Karachi","Islamabad")




        