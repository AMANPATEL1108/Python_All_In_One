from functools import reduce
a=[1,23,34,343,456,56,534,343,55,34,35]


def greter(a,b):
    if(a>b):
        return a
    return b

print(reduce(greter,a)) 