import random

# Ask the number for a random number between 1 - 10.

randNum = random.randint(1, 100)
guessesCount = 0
youGuess = 0
askForRestart = ""
restartGame = True

while randNum != youGuess or restartGame:
    youGuess = int(input("What is your guess? "))
    if randNum > youGuess:
        guessesCount += 1
        print("Guess higher.")
    elif randNum < youGuess:
        guessesCount += 1
        print("Guess lower.")
    else:
        guessesCount += 1
        print("You guessed it.")
        print()
        print(f"You have guessed {guessesCount} times.")
        print()
        askForRestart = input("Want to restart the game? ").lower()
        guessesCount = 0
    if askForRestart == "yes":
        restartGame = True
    else:
        restartGame = False

print()
print("Thank You for playing my game! It was great to have you experience it.")
