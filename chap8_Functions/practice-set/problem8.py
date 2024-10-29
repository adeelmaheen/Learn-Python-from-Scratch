# write a python function to print multiplication table of a given number.

n = int(input("Enter the number: "))

def multiply(n):
    for item in range(1,11):
        print(f"{n} X {item} = {n * item}")

multiply(n)
