# factorial(5)=5x4x3x2x1


def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)

n=int(input("Enter a Number"))
ans=factorial(n)
print(ans)