import random
import os


def guess_check():
    global CHOSEN_NUMBER,lives
    guess = int(input("Make a guess: "))
    if guess == CHOSEN_NUMBER:
        print(f"You got it! The answer was {CHOSEN_NUMBER}")
        quit()
    elif guess < CHOSEN_NUMBER:
        print("Too Low")
    elif guess > CHOSEN_NUMBER:
        print("Too High")
    print("Guess Again")
    lives -= 1
    print(f"You have {lives} attempts remaining to guess the number")


os.system('clear')

print("Welcome to the Number Guessing Game.")
print("I\'m thinking of a number between 1 and 100.")

CHOSEN_NUMBER = random.randint(1,100)

while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        lives = 10
        break
    elif difficulty == 'hard':
        lives = 5
        break
    else:
        print("You entered an invalid difficulty level")

while lives > 0:
    guess_check()
print(f"You\'ve run out of guesses. The Number was {CHOSEN_NUMBER}")