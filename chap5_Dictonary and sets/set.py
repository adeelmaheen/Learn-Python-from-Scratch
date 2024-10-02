# set is a collection of non-repetitive elements.
b:dict = {}              # {}    for dictionary
s = set()           # {}    for empty set 
s.add(1)            # {1}
s.add(2)            # {1,2}
# print(type(s),"S :", s) 
# print(type(b),"B :",b)


# Properties of sets
# 1. Sets are unordered   => Elements order does'nt matter
# 2. Sets are umindexed   => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets can not contain duplicates values.

# Operations on sets:
set_1 = {1,2,3,4}

# len(set_1) : Returns 4 , the length of the set.
# print(len(set_1))

# set_1.remove(2) : Updates the set set_1 and removes 2 from set_1
# set_1.remove(3)
# print(set_1)

# set_1.pop() : remove 1 element
#  Removes an arbitary element from the set and return the element removed.
# print(set_1.pop())
# print(set_1)

# set_1.clear() : empties the set set_1
# set_1.clear()
# print(set_1)

# set_1.union({2,11}) : 
# Returns a new set with all items from oth sets. {1,2,3,4,11} no duplicate value allow
# we can write .union() or pipe sign |

print(set_1.union({2,11}))

set_2 = {1,2,3,4}
set_3 = {5,6,7,8}
set_0 = set_2 | set_3
# print(set_0)

# set_1.intersection()
# finds comman elements 
# we can write .intersection() or end operator &

intersection_set1 = set_1.intersection(set_2)
intersection_set2 = set_2 & set_3
# print("intersection_set1 : .Intersection() ", a)
# print("intersection_set2 : & ", b)

# Difference() 
# Elements in one set but not the other set.
# we can write .difference() or - subtract sign

differece_set1 = set_2 - set_3
differece_set2 = set_1.difference(set_3)
print("Difference_set1 :" , differece_set1)
print("Difference_set2 :" , differece_set2)

# Symmetric difference
# Elements in other set but not in both.
# we can write .symmetric_difference or tilda sign ^
symmetric_set1 = set_2.symmetric_difference(set_3)
symmetric_set2 = set_1 ^ set_2
print("Symmetric_difference1 : ", symmetric_set1)
print("Symmetric_differenece2 : ", symmetric_set2)

# Update(iterable)
# adds one or more elements in the set
# no duplicate values allow in set

set_1.update([1,5,6,7,8,1])
print(set_1)

# len()
# length of a set
length_set1 = len(set_1)
print(length_set1)

# set comprehension
# similar to list comprehension, set comprehension provides a concise way to create sets.
# syntax
# { expression for  item in iterable if condition }
# expression: What to include in the new set.
# item : the item to itrate over.
# Iterable : The iterable to loop through (i.e, a list, range, etc)

squares = { x**2 for x in range(10)}
print("Squares : " , squares)

even_sqaures = { x**2 for x in range(20) 
                if x % 2 == 0}
print("Even_squares :" , even_sqaures)


