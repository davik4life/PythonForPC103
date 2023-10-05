# Get the users fav letter

heldWord = "commitment"

favLetter = input("Enter your favourite latter: ")
for letter in heldWord:
    if letter == favLetter.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")
