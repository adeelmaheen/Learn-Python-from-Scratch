# set is a collection of non-repetitive elements.
b:dict = {}              # {}    for dictionary
s = set()           # {}    for empty set 
s.add(1)            # {1}
s.add(2)            # {1,2}
print(type(s),"S :", s) 
print(type(b),"B :",b)


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
print(set_1)

# set_1.union({2,11}) : Returns a new set with all items from oth sets. {1,2,3,4,11}
print(set_1.union({2,11}))


