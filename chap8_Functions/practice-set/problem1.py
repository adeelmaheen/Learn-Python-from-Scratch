# write a program using functions to find greatest of three numbers.

a = int(input("Enter the Number"))
b = int(input("Enter the Number"))
c = int(input("Enter the Number"))
def greatest(a:int,b:int,c:int):
    if ( a>b and a>c):
        print(f"The greatest number is {a}")
    elif (b >a and b >c):
        print(f"The greatest number is {b}")
    elif ( c>a and c >b):
        print(f"The greatest number is {c}")

result = greatest(a,b,c)
