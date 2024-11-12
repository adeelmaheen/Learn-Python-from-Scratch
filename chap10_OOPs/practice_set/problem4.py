# add a static method in problem 2, to greet the user with hello

class Calculator:
    def __init__(self,num1):
        self.num1 = num1

    @staticmethod   
    def greet():
        print("Hello! How are you...")

    def sqaure(self):
        print(f'The square is: {self.num1 * self.num1}')
        
    
    def cube(self):

        print(f"The cube is: {self.num1 * self.num1 * self.num1}")
       
    
    def squareRoot(self):
        print(f"The squareRoot is: {self.num1 ** self.num1}")
       
    
calculate = Calculator(5)
calculate.greet()
calculate.cube()
calculate.sqaure()
calculate.squareRoot()