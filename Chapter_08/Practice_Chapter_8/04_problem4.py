def sum(a):
    if(a==0):
        return 0
    return a+sum(a-1)


n=int(input("Enter a Number:"))
ans=sum(n)
print(ans)