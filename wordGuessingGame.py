secretWord = "victor"
guessWord = ""
guessCount = 0
while secretWord != guessWord:
    guessWord = input("What is your guess? ").lower()
    guessCount += 1
    if secretWord != guessWord:
        print("Your guess was not correct.")
    else:
        print("Congratulations! You guessed it!")
        print(f"It took you {guessCount} guess(es)")
