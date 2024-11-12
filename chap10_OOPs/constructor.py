# __INIT__() Constructor

# __init__() is a special method which is first run as soon as the object is created.
# __init__() method is also known as constructor.
# It takes self argument and can also take

class Employee:
    salary = 3000
    designation  = "HR"
    language = "English"

    def __init__(self,name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language     #dunder method which is automatically called.
        print("I am a constructor method")

    def greet(self):
        print(f"I am a function with a self parameter.{self.designation}")
    
    @staticmethod
    def greet2():
        print("I am a funtion with a no self parameter")

maheen = Employee("Maheen",12000,"Urdu")
maheen.name = "Maheen Arif"
maheen.greet()
maheen.greet2()
print(maheen.name,maheen.designation,maheen.language)

