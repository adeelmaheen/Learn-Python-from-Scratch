# write a program to find out the line number where python is present from question 6 

with open("longFile.txt", "r") as f:
    content = f.readlines()

    lineNo = 1 
    for line in content:
        if ("python" in line):
            print(f"yes python is present in the Line Number: {lineNo}")
            break
        lineNo += 1
    else:
        print("Python is not present in the line")
        
