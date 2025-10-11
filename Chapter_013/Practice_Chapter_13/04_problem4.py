def deivisible5(n):
    if(n%5==0):
        return True
    return False

a=[1,23,34,3435,456,56,534,343,55,34,35]

f=list(filter(deivisible5,a))
print(f)