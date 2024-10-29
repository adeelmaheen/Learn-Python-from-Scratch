# write a python function to print first n lines of the following patteren:
#   ***
#   **              for n = 3
#   *

n = int(input("Enter the number: "))
def pattren(n):
    if ( n == 0):
        return 
    else:
      print("*" * n)
      pattren(n - 1)

pattren(n)
