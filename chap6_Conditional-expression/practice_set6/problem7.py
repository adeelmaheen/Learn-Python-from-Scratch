# write a program to find out weather a given post is talking about "Maheen" or not.

post = input("Enter your post here: ")

if ( "maheen" in post.lower()):
    print("This post is talking about Maheen")
else:
    print("This post is not talking about Maheen")
    