def main():
    try:
          a=int(input("Enter Number:"))
          print(a)
          return
    except Exception as e:
          print(e)   
          return 
    finally: # here before that return then that is not run then this is inmportuen after return also this is Run
           print("I am Inside finally")

print("Thank You")