# solving a problem by creating object is one of the most popular approches in programming. this is called )bject- Oriented Programming
# This concept focusing on using resuable code (Dry principle).

# CLASS
# A class is a blue print for creating object.

# Syntax:
# class Employee:   class name is written in general case.
#   Methods & Variables 

class Employee:
    name = str
    language = str
    salary = int

maheen = Employee()
print(maheen.name, maheen.language)


class Employee1:
    language1 = 'python'
    salary1 = 1200

# Instamt attributes
# an attribute that belongs as the instant object() Assuming the class that the previous example:
# Note: instance attributes take preference over class attributes during assigments & retrivals.
# when looking up for momina attributes it checks for the following.
# 1- Is attributes present in the object?
# 2- is attributes present in class?

momina = Employee1()
momina.salary1 = 12000
momina.language1 = "english"
print(momina.language1, momina.salary1)



# Object 
# An object is an instentations of a class.when class is defined a templates (into) is defined.Memory is allocated only after object instentations.
# Object of a given class can include the methods available to it without revealing the implementation detailed the user .
# Abstraction & Encapsulation

# Modelling a Problem in OOPs
# We identify the following in our program.
# 1- Noun -> Class -> Employee
# 2- Adjective -> Attributes -> name, age, salary
# 3- Verbs -> Methods -> getSalary(), increment()

# Class Attributes
# An attributes that belongs the class rather than a particular object.
# Example:

