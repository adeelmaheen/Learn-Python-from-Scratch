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
# print(dic_1, type(dic_1))

# Accessing key index
# print(dic_1["key"])

# Accessing all keys in dictonary variable.
# print(dic_1.keys())

# Accessing all items in the dictonary.
# print(dic_1.items())

# Accessing all values in the dictonary
# print(dic_1.values())

# update the dictonary  ( update and also add new items in dictonary )
# updates the dictonary with supplied key-value pairs.
dic_1.update({"key" : "Location" , "Location" : "Home" })
# print(dic_1)


# 1 way: get the dictonary key or value ( if not found say None )
print(dic_1.get("name"))
# print(dic_1.get("Ibrahim"))     # None not in the dictonary
# 2 way: use square braces[] to get key or value ( if not found through error ) 
print(dic_1["name"])
# print(dic_1["Ibrahim"])         # through error not in the dictonary


# clear() : Removes alll items in the dictonary
# dic_1.clear()
print(dic_1)

# copy() :  Return a shallow copy of the dictonary
copy_dic = dic_1.copy()
# print(copy_dic)

# fromkeys(iterable , value = None)
# creates a new dicyonary with keys from the iterable and values set to the value.
keys = ["a" , "b", "c" , "d"]
d = dict.fromkeys(keys,1)
# print(d)

sum = [ "Maheen" , "Momina" , "Ibrahim"]
k = dict.fromkeys(sum,3)
# print(k)

# pop(key,default = None) 
# Removes and returns the value for the specified key. if the key does not exist, it returns the default value.
dic_1.pop("name")
# print(dic_1)

# popitem()
# Removes and returns the last inserted key-value pair as atuple.
print(dic_1.popitem())

# setdefault(key,default =None)      same as update method
# Returns the value of the specified key. if the key does not exist, it inserts the key with the specified default value.
dic_1.setdefault("name2","Momina")
print(dic_1)

