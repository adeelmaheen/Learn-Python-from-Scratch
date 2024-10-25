'''
    *  *  *
    *     *             for n = 3
    *  *  *


'''

n = int(input("Enter the number: "))
for i in range(1,n+1):
    if (i == 0 or i == n):
        print("*" *(n) ,end="")
    else:
        print("*",end="")
        print(" "* (n-2), end="")
        print("*", end="")
    print("")


print( " Second one")
n = 3

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
