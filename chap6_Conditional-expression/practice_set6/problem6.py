# write a program to calculate the grade of a students from the marks. from the following scheme
# 90 - 100  => Ex
# 80 - 90  => A
# 70 - 80  => B
# 60 - 70  => C
# 50 - 60  => D
# 40 - 50  => Fail


marks = int(input("Enter your marks: "))

if ( marks <= 100 and marks >= 90):
    grade ="Execellent"
elif ( marks <= 90 and marks >= 80 ):
    grade = "A+"
elif ( marks <= 80 and marks >= 70 ):
    grade = "A"
elif ( marks <= 70 and marks >= 60 ):
    grade ="B"
elif ( marks <= 60 and marks >= 50 ):
    grade ="C"
elif ( marks <= 50 and marks >= 40 ):
    grade ="D"
elif ( marks <= 40 and marks >= 30 ):
    grade = "Fail"

print ("Your grade is : " , grade)