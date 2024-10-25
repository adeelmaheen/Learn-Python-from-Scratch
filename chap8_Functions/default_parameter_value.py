# we can have a value as default as default argumentin a function.
# if we specify name = " Maheen " in the containing def , this value is used when no argument is passed.

def sum ( a,b,c = 10):
    sum = a + b + c 

    return sum

defaulit_def = sum(12,22)
print(defaulit_def)

