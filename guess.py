import random

# Ask the number for a random number between 1 - 10.

# randNum = int(input("Pls enter a magic number between 1 - 10: "))
randNum = random.randint(1, 100)
youGuess = 0

while randNum != youGuess:
    youGuess = int(input("What is your guess? "))
    if randNum > youGuess:
        print("Guess higher.")
    elif randNum < youGuess:
        print("Guess lower.")
    else:
        print("You guessed it.")
