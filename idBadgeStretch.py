# Writing a Program that prompts users for their information.

firstName = input("Pls Enter your first name: ")
lastName = input("Pls Enter your last name: ")
email = input("Pls Enter your email: ")
phoneNumber = input("Pls Enter your Phone Number: ")
jobTitle = input("Pls Enter your Job Title: ")
idNumber = input("Pls Enter your ID Number: ")
hairColor = input("What is your Hair Color? ")
eyeColor = input("What is your Eye Color? ")
birthMonth = input("What is your Birth Month? ")
training = input("Have you completed your Training? ")

yourInfo = f"{lastName.upper()}, {firstName.lower()}\n{jobTitle.title()}\nID: {idNumber}\n\n{email.lower()}\n{phoneNumber}\n\n"
addInfo1 = f"Hair: {hairColor.title():15} Eyes: {eyeColor.title()}"
addInfo2 = f"Month: {birthMonth.capitalize():14} Training: {training.title()}"
line = "--------------------------------------------------"
print("\nThe ID Card is:")
print(line)
print(yourInfo)
print(addInfo1)
print(addInfo2)
print(line)
