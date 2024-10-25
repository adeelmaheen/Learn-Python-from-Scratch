# A function is a group of statements performing a specific task
# when a program gets bigger in size its complexitygrows, It gets difficult to program to keep on which pieces of  code is doing what!
# A function can be resued by the programmer in a given program any number of

# Syntax:
def function1():
    print("Hello Function")

#  This function can be called any numberof times, anywhere in the program 

# Function Call
# whatever we want to call a function, we put the names of the function followed by Parenthesis ( ) as follows.
function1()

# Function Defination
# the part containing the exact set of instructions which are executed during the function call.



def average_sum():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))

    avg = (a + b + c)/ 3
    print(avg)
    return avg

func_call = average_sum()

print("Function End!")

# Function with Argument:
# A function can accept some values it can work with. we can put these values in the paranthesis. where we call the function 
#  A function can return the values as shown below:

def greet(name):
    g = "hello" + name
    return g
v = greet("Maheen")
