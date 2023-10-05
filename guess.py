import random

# Ask the number for a random number between 1 - 10.

# randNum = int(input("Pls enter a magic number between 1 - 10: "))
randNum = random.randint(1, 100)
youGuess = int(input("What is your guess? "))

while randNum != youGuess:
    if randNum > youGuess:
        print("Guess higher.")
        youGuess = int(input("What is your guess? "))
    else:
        print("Guess lower.")
        youGuess = int(input("What is your guess? "))
print("You guessed it.")
