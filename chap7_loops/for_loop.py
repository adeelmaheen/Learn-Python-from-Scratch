# for loop
#  A for loop is used to iterate through a sequence like list, tuple or string [ iterables].
# syntax:

# FOR LOOP with List
l = [ 1, 7, 8]
for item in l:
    print(item)

#  Range function in Python
# The range() function in python is used to generate a sequence of number.
# we can also specify the start , stop and step-size as follows:
# range( start, stop, step-size)
# step-size is usually not used with range()

# An example demostrating range() function.
for i in range(0,7):    # range(7) can also be used. 
    print(i)            # print 0 to 6

# FOR LOOP with STRING
s = "Maheen"
for c in s:
    print(c)


d = 0
while ( d < 5):
    print("Maheen")
    d += 1

for v in range(4):          # agr 0 na likhe tw by default wo zero assume krleta hai or range ka end number alwys n-1 hota hai
    print("Hello For LOOP is executed")


#  hum tuple list string or integer pr iterate kr skte hn

#  For LOOP with TUPLE
tuple_1 = ("Maheen", False,1, "Hey")
for t  in tuple_1:
    print(t)
