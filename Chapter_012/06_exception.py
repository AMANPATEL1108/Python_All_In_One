try:
    a=int(input("Enter Number:"))
    print(a)

except ValueError as v:
    print("This is From Value Error")
    print(v)
except Exception as e:
    print(e)    

print("Thank You")