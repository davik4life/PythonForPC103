# Write a Python Program that does each of the following:

# Use a while loop to ask the user for a positive number (>= 0). Continue asking as long as the number is negative, then display the number. For example:

entNum = int(input("Please, type a positive number: "))
while not entNum >= 0:
    print("Sorry, that is a negative number. Please try again")
    entNum = int(input("Please, type a positive number: "))

print(f"The number is: {entNum}")
