# Ask a user for their first name and then Capitalize it.
firstName = input("What is your first name? ")
lastName = input("What is your last name? ")


# But for sentences, the title() function would Capitalize every word in the sentence.
# The capaitalize() function would only capitalize just the first word in the sentence.
answer = f"{lastName}, {firstName} {lastName}."
print(answer.title())
