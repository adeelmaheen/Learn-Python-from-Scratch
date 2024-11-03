# The random access memory is volatile, and all its contents are lost once a program terminates
#  in order to persist  the data forever, we use files.

#  a file is data stored in  a storage device. A python program can talk to the file ny reading 
# content from it and writing content to it.

#  programmer  => computer program written in python  => [ write  -->  read <-- ] File
# RAM = volatile
# HDD / SDD = non-volatile 

#                                       Types of files.
# There are two types of files:
#  1. Text files (.txt, .c etc) 
#  2. Binary files (.iog, .dat, etc)
# python has a lot of functions for reading, updating and deleting files.


# Opening a file:
# python has an open() function for opening files. It takes 2 parameters:  filename & made.

# open("filename" , "mode of opening(read mode)")
# open(" this.txt" , "r")

st = " hey"

f = open("myfile.txt","w")
f.write(st)
f.close()

# Basic Steps in File I/O
# Open the File: Use the open() function.
# Read or Write: Use methods like read(), readline(), write().
# Close the File: Use close() to release the file.



# Mode	Description
# 'r'	Read (default mode)
# 'w'	Write (overwrites the file)
# 'a'	Append (adds to the end of the file)
# 'r+'	Read and write

