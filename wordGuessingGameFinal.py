# In added the word that had been guessed and I printed it at the success of the game.

import random

# Define the secret word
secretWord = "python"

# Initialize the variables
numGuesses = 0
guessedWord = ["_"] * len(secretWord)
print("Your hint is: ", end="")
print(" ".join(guessedWord))

while True:
    # Display the current state of the guessed word

    guess = input("What is your guess: ").lower()

    # Check if the guess has the same length as the secret word
    if len(guess) != len(secretWord):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        numGuesses += 1
        continue

    # Update the number of guesses
    numGuesses += 1

    # Check each letter in the guess
    hint = []
    for i in range(len(secretWord)):
        if guess[i] == secretWord[i]:
            guessedWord[i] = guess[i].upper()
        elif guess[i] in secretWord:
            guessedWord[i] = guess[i]
        else:
            guessedWord[i] = "_"

    # Check if the word has been guessed correctly
    if "".join(guessedWord) == secretWord.upper():
        print("Congratulations! You guessed it!: ")
        print(f"The word is {secretWord}")
        print(f"It took you {numGuesses} guesses.")
        numGuesses += 1
        break

    # Provide hint
    hint = " ".join(guessedWord)
    print("Your hint is:", hint)
