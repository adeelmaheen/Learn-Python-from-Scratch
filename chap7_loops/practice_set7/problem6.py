# write a program to calculate the factorial of a given number using for loop.

user_input = int(input( " Enter your Number: "))

product = 1
for i in range(1,user_input + 1):
    product = product * i

print(f"The Factorial of {user_input} is: ", product)
