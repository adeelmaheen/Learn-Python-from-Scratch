# write a python function which converts inches to cms.
# 2.54

inches = int(input("Enter the value in inches: "))
def inches_to_cm(inches):
    return  inches * 2.54


             
print(f" The corresponding value in cms is {inches_to_cm(inches)}")
