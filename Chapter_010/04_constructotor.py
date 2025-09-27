class Employee:
    language="Python"
    salary=1202120

    def __init__(self,name,salary,language): #As a dunder method as a Automatically Called
        self.name=name
        self.language=language
        self.salary=salary  
        print("I am Creating a Object")

    def getInfo(self):
        print(f"THe Languale is {self.language}. The Salary is {self.salary}")

    @staticmethod  #Dont Want to Objet for this anotation
    def greet():
        print("Good morning")


aman=Employee("aman",120000,"Java")
print(aman.name,aman.salary,aman.language)
# aman.language="Java"
# print(aman.salary,aman.language)

# rohan=Employee()
# rohan.language="Js"
# print(rohan.salary,rohan.language)

# aman.getInfo(aman)
# aman.greet()
# aman.getinfo(aman)