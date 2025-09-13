
def gretest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    else:
        return c
        

a=int(input("Enter Number:"))
b=int(input("Enter Number:"))
c=int(input("Enter Number:"))

ans=gretest(a,b,c)
print(ans)