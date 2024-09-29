# Check that type( ) can not be change in python

num1 : int  = 55
print(type(num1))
a_1 = str(num1)      # integer to string
print(type(a_1))

name : str = "Maheen"
print(type(name))
a_2 = int(name)      # string tyoe cant be converted in any any type 
print(type(a_2))

