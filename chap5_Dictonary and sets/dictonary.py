# Dictonary is a collection of key value pair.

# Properties of python dictonaries.
# 1. it is unordered
# 2. it is mutable.
# 3. it is indexed.
# can not contain duplicate keys.


dic_1 = {
    "key" : "value",
    "name" : "Maheen",
    "Marks" : 99,
    "list" : [1,3,9],
    "Student" : True
}

# ====================================    Dictonary methods.    ================================

# check type of dictonary
print(dic_1, type(dic_1))

# Accessing key index
print(dic_1["key"])

# Accessing all keys in dictonary variable.
print(dic_1.keys())

# Accessing all items in the dictonary.
print(dic_1.items())

# Accessing all values in the dictonary
print(dic_1.values())

# update the dictonary  ( update and also add new items in dictonary )
dic_1.update({"key" : "Location" , "Location" : "Home" })
print(dic_1)

# get the dictonary key or value ( if not found say None )
dic_1.get("name")
print(dic_1) 