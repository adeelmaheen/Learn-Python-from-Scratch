# write a program to read text from the given file "poems.txt" and find out wheather it contains the word "twinkle"

f = open("poems.txt","r")
content = f.read()
if ("twinkle" in content):
    print("The word twinkle is presentr in the conten")
else:
    print("The word twinkle is not present in the content")
f.close()
