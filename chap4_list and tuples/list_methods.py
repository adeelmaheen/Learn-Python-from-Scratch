# List Methods:
list_1:list =[1,8,7,2,21,15,1,1]

# append an element to a list:
list_1.append(6)
print(list_1)

# insert an element at a specific position
list_1.insert(2,"A")
print(list_1)

#extend a list by adding multiple elements
list_1.extend([20,10,25])
print(list_1)

#remove an element from a list
list_1.remove('A')
print(list_1)

#pop an element from a list
a= list_1.pop()
print(a)
print(list_1)

#get the index of an element (if not found through error)
list_1.index(1)
print(list_1)

# count occurenece of an element
count = list_1.count(1)
print(count)

# sort a list
list_1.sort()
print(list_1)

# reverse a list
list_1.reverse()
print(list_1)

# clear a list
# list_1.clear()
# print(list_1)

# list comprehension ( to create lists based on existing lists)
squares = [ x**2 for x in list_1]
print(squares)

#check if an element exists in a list
if 1 in list_1:
    print("1 is in the list")


#sum() for adding list int values only not string values
my_list : list = [9,8,7,6,5]
sum1 = sum(my_list)
print(sum1)