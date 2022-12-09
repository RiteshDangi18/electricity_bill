#write a function to calculate the amount of electricity bill
class bill:
    def __init__(self,x,y,z):
        self.x=u
        self.y=y
        self.z=z
    def amount(self):
        if 0<=self.x<=100:
            print("address: ",self.y)
            self.z=self.x*12
            print("amount=",self.z)
        elif 0<=self.x<=200:
            print("address: ",self.y)
            self.z=(self.x-100)*17+100*12
            print("amount=",self.z)
        else:
            print("address: ",self.y)
            self.z=(self.x-200)*25+100*17+100*12
            print("amount=",self.z)

x=int(input("enter the no of unit consumed: "))
y=input("enter the address: ")
a=bill(x,y,z=0)
a.amount()
