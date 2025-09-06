a=int(input("Enter your age:"))

#If Statment 1
if(a%2 ==0):
     print("age is Even")

#If Statment 2
if(a>18):
     print("You are above the age of consent")
elif(a<0):
     print("You are Entering Invalid Negative age")
elif(a==0):
     print("You are Entering 0 age")
else:
     print("You are below the age of consent")


