# Inheritance
# Inheritance is a way of creating a new class from an exsisting class.

# TYPES OF INHERITANCE:
# 1- single Inheritance
# 2- multiple Inheritance
# 3- multiLevel Inheritance

# SINGLE INHERITANCE:
# single inheritance occurs ehen child class inherits only a single parent class.
#        Base 
#         ||
#       Derived


# Syntax:
class Employee:             # base class
    company = "ITC"
    def show(self,name,salary):
        self.name = name
        self.salary = salary
        print(f" The name is {self.name} and the salary is {self.salary} ")

# class Programmer:               # copy past whic is not good
#     company = "KCC"
#     def show(self,name,salary):
#         self.name =name
#         self.salary = salary
#         print(f"The name is {self.name} and the salary is {self.salary}")
    
#     def showLanguage(self,name,language):
#         self.name = name
#         self.language = language
#         print(f"The name is {self.name} and she is good in {self.language} language.")


class Programmer(Employee):         # inheritance class
    company = "KCC"
    def language(self,name,language):
        self.name = name
        self.language = language
        print(f"The name is {self.name} and she is good in {self.language} language ")
    
baseClass = Employee()
inheritanceClass = Programmer()

print(baseClass.company,inheritanceClass.company)
baseClass.show("Maheen",50000)
inheritanceClass.language("Maheen","Python")


# we can use the method and attributes of "Employee" in "Programmer" object.
# Also we can overwrite  or add new attributes and methods in "Programmer" class.







