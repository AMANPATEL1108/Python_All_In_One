def myFunc():
    print("Hellow World")


if __name__ == "__main__":
    #if this code is directly executed by running the file its present in
    print("We are Directly Running")
    myFunc()
    print(__name__) 

#After adding this method that is print a when run this __main__ 
# if not running from here afetr adding this if statment code then that is a not print anything