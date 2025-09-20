import random

def game():
    print("You are in a game")
    score = random.randint(1, 62)
    
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
        
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your Score is: {score}")
    
    if score > hiscore:
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score
