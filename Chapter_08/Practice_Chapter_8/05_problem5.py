
def pattern(a):
    if(a==0):
        return
    print("*"*a)
    return pattern(a-1)



n=int(input("Enter a Number:"))
print(pattern(n))