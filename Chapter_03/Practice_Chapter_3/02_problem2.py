
name=input("Enter Your Name:")
date=input("Enter Date:")

# letter='''
#     Dear {name},
#     YOur are Selected
#     {date}
# '''

letter=f'''
    Dear <|Name|>,
    Your are Selected
    <|Date|>
'''



print(letter.replace("<|Name|>","Aman").replace("<|Date|>","25/04/2003"))