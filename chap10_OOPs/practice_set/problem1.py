# create a class "Programmer " for storing information of few programmers working at Microsoft.

class Programmers:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

programer1 = Programmers("Maheen",50000,12345)
print(programer1.name,programer1.company,programer1.salary,programer1.pin)

programer2 = Programmers("Momina",55000,12346)
print(programer2.company,programer2.name,programer2.pin,programer2.salary)



