class Employee:
    language="Python"
    salary=1202120

    def getInfo(self):
        print(f"THe Languale is {self.language}. The Salary is {self.salary}")

    @staticmethod  #Dont Want to Objet for this anotation
    def greet():
        print("Good morning")


aman=Employee
aman.language="Java"
print(aman.salary,aman.language)

rohan=Employee()
rohan.language="Js"
print(rohan.salary,rohan.language)

aman.getInfo(aman)
aman.greet()
# aman.getinfo(aman)