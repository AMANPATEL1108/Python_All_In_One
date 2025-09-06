p1="Make a lot of mony"
p2="buy now"
p3="subscribe this"
p4="clcik this"



message=input("Enter comment")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This is Spam")
else:
    print("Not Spam")