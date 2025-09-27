class Programmer:
    comany="Microsoft"

    def __init__(self,name,salary,pincode):
        self.name=name
        self.salry=salary
        self.pincode=pincode


p=Programmer("Aman",1222222,381256)
print(p.name,p.salry,p.comany)