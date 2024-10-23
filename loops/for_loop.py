# for loop
#  A for loop is used to iterate through a sequence like list, tuple or string [ iterables].
# syntax:
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

s = "Maheen"
for c in s:
    print(c)
