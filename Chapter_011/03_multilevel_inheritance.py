class Employee:


    company="ITC"
    name="Default Name"


    def show(self):
        print(f"The name is {self.name} and Company is {self.company} ")


class Coder(Employee):
     language="Py"
     def printLanguage(self):
          print(f"out of all language here is Your Langaueg {self.language}")

class Programmer(Coder):
    company="ITC Info"

    def showlanguage(self):
             print(f"The name is {self.company} and language is {self.language} ")

# a=Employee()
# b=Programmer()
# b.show()
# b.showlanguage()
# b.printLanguage()
p=Programmer()
p.show()
p.printLanguage
p.showlanguage()
# print(a.company,b.company)