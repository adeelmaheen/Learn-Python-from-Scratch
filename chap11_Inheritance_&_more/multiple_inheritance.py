# MULTIPLE INHERITANCE:
# multiple inheritance occurs when the child class inherits from more that one parent classess.

#   parent1 -----------  parent2
#      |____________________|
#                 |
#               child

class Employee:
    company = "ITC"
    def detail(self,name,designation,salary):
        self.name = name
        self.designation = designation
        self.salary = salary
        print(f"The name of the employee is : {self.name} and their designation is : {self.designation} and their salary is {self.salary}")

    def payment(self):
        print("the payment is done.")
    
class Coder:
    language = "Python"
    def checkLanguage(self):
        print(f"Out of all language here is your langugae {self.language} ")
    
class Programmer(Employee,Coder):           # multilpe inheritance
    company = "ITC Info Tech"
    def showLanguage(self):
        print(f"The name of the company is {self.company} amd the coder language is {self.language}")

employee = Employee()
coder = Coder()
programmmer = Programmer()
programmmer.checkLanguage()
programmmer.showLanguage()
programmmer.detail("Maheen","HR Manager",55000)

