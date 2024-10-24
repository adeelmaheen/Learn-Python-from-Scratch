# write a program to finD the sum of first natural numbers in while loop
input_user = int(input("Enter the Number: "))

i = 1
sum = 0
while(i <= input_user):
    sum += i
    i += 1
    
print(sum)