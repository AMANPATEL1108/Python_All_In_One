class Demo:
    a=4

o=Demo()
print(o.a) #Intance Attribute
o.a=0
print(o.a)  #Instance Change
print(Demo.a)  #Class Attribute Can not Change
