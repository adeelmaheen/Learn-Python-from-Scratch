# self Parameter
# self refer to the instance of the class. It is automatically passed with a function call from an object

class Employee:
    language = "Python"
    salary = 3000
    designation = "HR"

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good Afternoon!")
    
    @staticmethod
    def greet2():
        print("Hi Im without self parameter which means im staticmethod")

maheen = Employee()
maheen.language = "Javascript"      # this is an instant attribute
maheen.getInfo()
maheen.greet()
maheen.greet2()


# STATIC METHOD 
# @staticmethod
# means yh koi self parameter nh leta hai yh likhne se hum mark krte hn k as a function k yh koi parameter nh lega


