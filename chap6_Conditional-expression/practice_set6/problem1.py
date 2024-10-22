# Write a program to find the gretest of four numbers entered by the user.
a1 = int(input("Enter your age: "))
a2 = int(input("Enter your age: "))
a3 = int(input("Enter your age: "))
a4 = int(input("Enter your age: "))

if (a1 > a2 and a1 > a3 and a1 > a4):
    print("The gretest value is A1", a1)
elif (a2 > a1 and a2 > a3 and a2 > a4):
    print("The gretest value is A2 ",a2)
elif (a3 > a1 and a3 > a2 and a3 > a4):
    print("The gretest value is A3", a3)
elif (a4 > a1 and a4 > a2 and a4 > a3):
    print("The gretest value is A4", a4)
    