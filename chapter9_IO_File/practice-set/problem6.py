# write a program to mine long file and find out wheather it contains "python".
word = "python"

with open("longFile.txt","r") as f:
    content = f.read()

if (word in content):
    print("Yes Python word is present ")
else:
    print("No python is not present")