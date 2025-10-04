a=89
def fun():
    global a  #after adding this that is globally set a a else not set out of this statment code that is not set that value ok
    a=3
    print(a)

fun()
print(a)
