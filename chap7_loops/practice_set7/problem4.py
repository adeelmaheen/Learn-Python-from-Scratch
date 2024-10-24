# write a program to find wheather a given number is Prime or not.

input_user = int(input("Enter your number: "))

for x in range(2,input_user):
    if(input_user % x == 0):
        print("The number is not Prime: " , input_user) 
        break
else:
    print("Number is Prime: ",input_user )