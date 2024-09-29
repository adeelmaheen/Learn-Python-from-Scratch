# Tuples are immutable meaning, their content can not be changed once defined.
# Howerver, you can perform various operations on tuple

# create a tuple 
my_tuple:tuple = (1,2,3,4,5,6,7,8,9,10)

# Accessing Elements (by index)
print(my_tuple[0])
print(my_tuple[7])
print(my_tuple[-1])    # excess last element

# slicing a tuple (to get a subset)
print(my_tuple[1:3])
print(my_tuple[2:7])

# concatenating tuple ( + )
tuple1 : tuple = (1,2,3,4)
tuple2 : tuple = ( 5,6,7,8,)
concat_tuple = tuple1 + tuple2

tuple3 : tuple = ("A","B", "C")
tuple4 : tuple = ("D", "E", "F")
check = tuple3 + tuple4

merge_1 = tuple1 + tuple3

print(concat_tuple)
print(check)
print(merge_1)


# Repeating a tuple ( * )
repeated_tuple = tuple1 * 3
print(repeated_tuple)

# Checking for membership ( in )
print( 3 in tuple3 )
print( 1 in tuple1 )

# Length of a tuple ( len() )
print(len(tuple1))
print(len(tuple2))
print(len(tuple3))
print(len(tuple4))

# Iterating over a tuple ( for loop )
for item in tuple4 : 
 print(item)

for item in tuple2 :
 print(item)

for x in tuple3 :
 print(x)

# Unpacking a tuple ( seprate variable )

a = tuple4
print(a)


# ========================   Tuples Methods ======================================

# count()
print(tuple1.count(3))
print(tuple3.count(2))

#index()
print(tuple1.index(4))
print(tuple3.index("B"))

# ======================= Nested Tuple ===========================================
nested_tuple = (1,2,(3,4,5),6,7)
print(nested_tuple)
print(nested_tuple[2])