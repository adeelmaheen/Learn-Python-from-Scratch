# Recursion is a function which calls itself.
# It is used to directly , use a mathematical formulas function 

#                           or

#  a recursion function is a function that calls itself in order to solve a problem.
#  The function keeps calling itself with smaller or simpler inputs until it reaches 
# a base condition, which stops the recursion.

# Key Concepts of Recursion:
# Base Case: This is the condition that stops the recursion. Without a base case, the function would call itself indefinitely, resulting in an error.
# Recursive Case: The part of the function where it calls itself to work towards the base case.

def factorial(n):
   
    if (n == 1):
        return 1
    else:
      return  n * factorial(n-1)

n = int(input("Enter the number you want of Factorial: "))    
result = factorial(n)
print(f"The factorial of {n} is {result}")

