#  Break Statements:
# break is used to come out of the loop when encountered. It instructs the program to exit the loop now.

for i in range(50):
    if ( i == 25):
        break           # exit the loop right now
    print(i)



# Continue Statements:
# continue is used to stop the current iteration of the loop and continue with the next one. It instructs the Program to " to skip this iteration".

l = ["Hi", "Bye", "Good", "Night"]
for a in l:
    if (a =="Good"):
        continue        # skip this iteration
    print(a)


# Pass Statement;
# pass is a null statement in Python.
# It instructs to " do nothing "

for x in range(10):
    pass


z = 0
while (z < 20):
    print("Pass Statement")
    z  += 1