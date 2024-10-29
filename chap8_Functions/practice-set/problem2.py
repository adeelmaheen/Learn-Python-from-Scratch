# write a python program using function to convert Celsius to Fahrenheit.
#  c / 5 = f - 32 / 9
#  C = 5 * f - 32 / 9

f = int (input( "Enter temperature in F: "))

def celsius(f):
    result = 5 * f - 32 / 9
    return round(result,2)
print(f"{celsius(f)} Degree C ")


