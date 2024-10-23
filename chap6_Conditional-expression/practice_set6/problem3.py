# A span comment is defined as a text containing following keywords.
# write a program to define these spams.
# "make a money now " , "buy now" , "click this" , " subscribe this"

phrase1:str = "make a money now"
phrase2 :str = " buy now"
phrase3 :str = "click this "
phrase4 : str = "subscribe this"

message = input("Enter your message:" )

if ((phrase1 in message) or (phrase2 in message) or (phrase3 in message) or (phrase4 in message)):
    print("This message is a spam")
else:
    print("This message is not spam ")


                

