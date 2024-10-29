# write a recurcive function to calculate the sum of first n natural numbers.

n = int(input("Enter the number: "))
def natural_1(n):
    if ( n == 1):
        return 1
    else:
        result = n + natural_1(n - 1)
        return result



result_num = natural_1(n)
print(result_num)
