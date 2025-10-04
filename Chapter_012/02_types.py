from typing import List,Union,Dict,Tuple

n:int=5

name : str = "Aman"


def sum(a:int ,b:int )-> int:
    return a+b

print(sum(3,5))


#Imported from typing 
#List
numbers:List[int]=[1,2,3,4,5,6,7]
#Tuple
person:Tuple[str,int]=("Aman",7)
#Dict
scores:Dict[str,int]={"Alic":90,"Bob":85}
#Union
identifier:Union[int,str]="ID123"
identifier=12345
