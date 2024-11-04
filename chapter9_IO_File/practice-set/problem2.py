# The game() function in a program lets a user play a game and returns the score as an integer.
#  you need to read a file "Hi-score.txt" which is either blank or contains the previous Hi-score
#  you need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

import random

def game():
    print("Welcome to generate a random number!....")
    score = random.randint(1,5)
    # fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print((f"Your score: {score}"))
    if (score > hiscore ):
        with open("hiscore.txt", "w") as f:
             f.write (str(score))

    return score

game()

        