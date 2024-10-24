# write a program to print multiplication table of a given number using for loop.

user_input = int(input("Enter the number: "))
x = 1
for x in range(1,11):
    print(f" {user_input} X {x} = { user_input * x} ")
     