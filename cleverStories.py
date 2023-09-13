# The Story to be used...

"""
The other day, I was really in trouble. It all started when I saw a very
[adjective] [animal] [verb] down the hallway. 
"[exclamation]!" I yelled. But all
I could think to do was to [verb] over and over. Miraculously,
that caused it to stop, but not before it tried to [verb]
right in front of my family.
"""

# Define the variables to hold user inputs
adjective = input("Enter an adjective: ")
animal = input("Enter the name of an animal: ")
verb = input("Enter a verb: ")
exclamation = input("Enter an exclamation word: ")
verb2 = input("Enter a verb: ")
verb3 = input("Enter a verb: ")


# Store the story into a variable as a formated string.
statement1 = f"The other day, I was really in trouble. It all started when I saw a very\n{adjective} {animal} {verb} down the hallway."

# Store the second part of the story into a variable as a formated string.
statement2 = f"\"{exclamation.capitalize()}!\" I yelled. But all\nI could think to do was to {verb2} over and over. Miraculously,\nthat caused it to stop, but not before it tried to {verb3} right in front of my family."

# Display to the user.
print(statement1)
print()
print(statement2)
