# can you change the self.parameter inside a class to something else (say "harry"). Try changing self to "slf" or "Maheen" and see the effects.

# yes we can use any word in the replace of self parameter but its just unprofessional or readblility is not good.

from random import randint

class Train:
    def __init__(slf,trainNo):
        slf.trainNo = trainNo

    def book(maheen,fromWhere,whereTo):
        maheen.fromWhere = fromWhere
        maheen.whereTo = whereTo
        print(f"Ticket is booked in train no: {maheen.trainNo} from {maheen.fromWhere} to {maheen.whereTo} ")

    def getStatus(self):
        print(f" Train no: {self.trainNo} is running on time")
    
    def getFare(self,fromWhere,whereTo):
        print(f"Ticket fare in train no: {self.trainNo} from {fromWhere} to {whereTo} is {randint(222,5555)}")

train = Train(123999)
train.book("Karachi","Islamabad")
train.getStatus()
train.getFare("Karachi","Islamabad")




        