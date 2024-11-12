# write a class "calculator" capable of finding square, cube and square root of a number.
class Calculator:
    def __init__(self,num1):
        self.num1 = num1
        

    def sqaure(self):
        print(f'The square is: {self.num1 * self.num1}')
        
    
    def cube(self):

        print(f"The cube is: {self.num1 * self.num1 * self.num1}")
       
    
    def squareRoot(self):
        print(f"The squareRoot is: {self.num1 ** self.num1}")
       
    
calculate = Calculator(5)
calculate.cube()
calculate.sqaure()
calculate.squareRoot()


    