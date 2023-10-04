# Use a while loop, to simulate a child asking their parent for a piece of candy. Have the program
# keep looping until the user answers "yes", then have the program output "Thank you."

answer = ""
while answer != "yes":
    answer = input("May I have a piece of candy?: ")

print("Thank you.")
