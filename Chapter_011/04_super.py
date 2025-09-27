class Employee:
    def __init__(self):
         print("Constructor of Employee")
    a=1

class Coder(Employee):
     def __init__(self):
        super().__init__()
        print("Constructor of Coder")
     b=2

class Programmer(Coder):
     def __init__(self):
         super().__init__()
         print("Constructor of Programmer")
     c=3

p=Programmer()
print(p.a,p.b,p.c)