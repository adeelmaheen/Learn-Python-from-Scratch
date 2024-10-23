#  write a program to find out wheather a sstudents has passed or failed if it required as total 40% in atleast 33% in each subject to pass . assume 3 students and take marks as an input from the user.

marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 1: "))
marks3 = int(input("Enter marks 1: "))

#  check for the total percentage
total_percentage = ( 100 * ( marks1 + marks2 + marks3)) / 300

if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("You are passes ", total_percentage)
else:
    print("You are failed")
    


