# String
# string is a data type in python
# string is a sequence of a characters enclosed in quotes.
# we can primarily write a string in these three ways.

a = "Maheen"            # single quote string
b = 'Maheen'            # double quote string
c = ''' Maheen '''      # triple quote string

# String Slicing
# A string in python can be sliced for getting a part of the strings.
# string is in immutable we cant change the character of a string later
# Consider the following string:

Name                  = " M A H E E N "        # string characters
index                 = " 0 1 2 3 4 5 "        # index start with 0
negative_indexing     = "-5 -4 -3 -2 -1"       # negative indexing starts from end 
length                = " 1 2 3 4 5 6 "        # length start with 1

# stings are immutable which means the existing string will not change it returns a new string. list are mutable means that they can replace the existing list 

# string functions and methods.

# slice()   
# name[index_start : index_end]  end index is not included
# name[start_index : go_on_that_index : skip_value ] 
slice_string = "maheen arif"
first_name = slice_string[0:6]
last_name = slice_string[7:11]
print(first_name)
print(last_name)
skip_value = slice_string[2:7:3]
print(skip_value)

#len()
name = "Momina"
print(len(name))

# string.endswith('character')
ends_with = name.endswith("a")
ends_with = name.endswith("e")
print(ends_with)

# string.stratswith('character')
start_with = name.startswith('m')
start_with = name.startswith('M')
print(start_with)

#string.count("character")
count_character = name.count("M")
count_character = name.count("a")
print(count_character)

#string.capitalize()
name1 = "momina"
name2 = name1.capitalize()
print(name2)

#string.find("character/word")
message = "My name is momina adeel ahmed"
check_1 = message.find("maheen")
check_1 = message.find("adeel")
print(check_1)

#string.replace(old word , new word)
check2 = message.replace("adeel ahmed","maheen")
print(check2)

#string.lower()
new_message = "MY NAME IS MAHEEN ARIF"
check_3 = new_message.lower()
print(check_3)

#string.upper()
check_4 = check_3.upper()
print(check_4)

#string.strip()
my_name = "   Maheen  Arif  "
print(my_name)
print(my_name.strip())

#string.join()
join_1 = 'Muhammad'
join_2 = 'Ibrahim'
print("  ".join(join_1)) 
print(" : ".join(join_2))

#string.split(seprator)
print(join_2.split())

#string.formar()
s = "Hello {}"
c = s.format("world")
print(c)

#string.encode()
e = "hello"
print(e.encode())

#string.format_map(mapping)
m = "hello , {name}"
print(m.format_map({"name":"Momina"}))


# Escape sequence character
# \n new line,  /t tab, \; single quote, \\ back slash

a = "Good Morning! \n Momina \t How are you"
print(a)