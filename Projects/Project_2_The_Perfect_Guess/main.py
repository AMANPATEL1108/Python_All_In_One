import random

n=random.randint(1,100)
a=-1
guesses=1
while(a!=n):
    a=int(input("Guess a Number"))
    if(a>n):
        print("Lowe Number Please")
        guesses+=1
    elif(a<n):
        print("Higher Number Please")
        guesses+=1

print(f"You Have guessed the number {n} correctly in {guesses} attempts")