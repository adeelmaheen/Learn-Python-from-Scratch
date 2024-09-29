# Write a program to accept , marks of 6 students and display them in a sorted manner.

marks : list = [ ]


ask_user1 = int(input(" Enter your marks ..."))
marks.append(ask_user1)


ask_user2 = int(input(" Enter your marks ..."))
marks.append(ask_user2)


ask_user3 = int(input(" Enter your marks ..."))
marks.append(ask_user3)


ask_user4 = int(input(" Enter your marks ..."))
marks.append(ask_user4)


ask_user5 = int(input(" Enter your marks ..."))
marks.append(ask_user5)


ask_user6 = int(input(" Enter your marks ..."))
marks.append(ask_user6)


marks.sort()
print(marks)
