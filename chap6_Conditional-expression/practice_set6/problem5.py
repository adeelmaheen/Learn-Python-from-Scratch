# write a program which finds out weather a given names is present in the list or not

name_list : list = [ "Maheen ", "Momina ", "Muhammad ", "Ibrahim "]
names = input("Enter your name :")

if (names in name_list):
    print("Your name is in the List: ", names)
else:
    print("Your name is not in the list: ", names)

 