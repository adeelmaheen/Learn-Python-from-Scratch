# In Python programming , we must be able to execute instructions on a conditions being met.
# Like sometimes we want to play PUBGcin our phone if the day is sunday.
# sometimes we go hacking if our parents allow
# All these dissicions which depends on a condition neing met.
# IF ELSE , ELIF in python:
# we can use comparision , logical operator, in function ,loop , functions in it. 
#  if else and elif statements are a manuallly decision taken byy our program due to certain condition in our code.

# synatx : 

# if (condition1) :
#     print("Yes")
# elif (condition2):
#     print("No")
# else:
#     print("otherwise")


a = int(input("Enter yor age : "))
if (a >= 18 ):
    print("You are above the age of consent")
elif ( a < 0):
    print("You enter the invalid age!")
else:
    print("You are below the age of consent ")
