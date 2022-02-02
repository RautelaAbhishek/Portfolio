import random

player = input("Rock Paper Scissors.\nWhat do you choose to throw out?(Rock,Paper or Scissors)\n").lower()
ai = random.randint(0,2)
options = ["rock", "paper", "scissors"]
if (player not in options):
    print("You entered an invalid option")
else:
    print("The computer threw out " + options[ai])
    playerNum = options.index(player)
    if (playerNum == 0 and ai == 2):
        print("You Win")
    elif (playerNum == 2 and ai == 0):
        print("You Lose")
    elif (ai > playerNum):
        print("You Lose")
    elif (playerNum > ai):
        print("You Win")
    else:
        print("It\'s a Tie")





