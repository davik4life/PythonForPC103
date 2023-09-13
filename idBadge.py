# The oneliner code below also works okay, but it is not readable and easy on the eye.
# yourInfo = f"{lastName.upper()}, {firstName.lower()}\n{jobTitle.title()}\nID: {idNumber}\n\n{email.lower()}\n{phoneNumber}"


# Writing a Program that prompts users for their information.

firstName = input("Pls Enter your first name: ")
lastName = input("Pls Enter your last name: ")
email = input("Pls Enter your email: ")
phoneNumber = input("Pls Enter your Phone Number: ")
jobTitle = input("Pls Enter your Job Title: ")
idNumber = input("Pls Enter your ID Number: ")
yourInfo = f"{lastName.upper()}, {firstName.lower()}\n{jobTitle.title()}\nID: {idNumber}\n\n{email.lower()}\n{phoneNumber}"
line = "--------------------------------------------------"
print("\nThe ID Card is:")
print(line)
print(yourInfo)
print(line)
