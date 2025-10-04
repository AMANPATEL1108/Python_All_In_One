a=int(input("Enter a Number a:"))
b=int(input("Enter a Number b:"))


if(b==0):
    raise ZeroDivisionError("Hey We can Not Divide By Zero")
else:
    print(f"The Division a/b is {a/b}")