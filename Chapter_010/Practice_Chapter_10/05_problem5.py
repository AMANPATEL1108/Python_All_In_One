import random
class Train:

    def __init__(self,trainNo):
            self.trainNo=trainNo

    def book(self,fro,to):
        print(f"Ticket is Booked in train No : {self.trainNo} from {fro} to {to}")

    def getStatus(self):
                print(f"train No : {self.trainNo} Is Sucessfully run on Time")

    def getFare(self,fro,to):
                print(f"Ticket is Fare in train No : {self.trainNo} from {fro} to {to} is {random.randint(22,555)}")


t=Train(121212)
t.book("Ah","Bh")
t.getStatus()
t.getFare("Ah","Bh")