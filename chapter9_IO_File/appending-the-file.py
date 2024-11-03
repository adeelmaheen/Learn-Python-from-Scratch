
# Appending the file
# Open the file using open(filename, mode).
# Use write() to add data or read() to get data.
# Close the file using close() (or use with to handle this automatically).

with open("example.txt","a") as file:
    file.write("Im so upset \n")
    file.write("Allah please reso;ve me all problems \n")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
    