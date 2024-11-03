# Using with is a better way to handle files because it automatically closes the file
#  after the block of code is executed.


# writing a file using "with"

with open("example3.txt","w") as file3:
    file3.write("im third file of I/O using 'with' \n")
    file3.write("Im not feeling well")

# reading the entire file using 'with'

with open("example3.txt", "r") as file3:
    content3 = file3.read()
    print(content3)
    


