# Write a program that does the following:

# Prompt the user for their age. Convert it to a number, add one to it, and tell them how old they will be on their next birthday.
age = input("What is your Age?: ")
intAge = int(age) + 1
print(f"On your next Birthday, you will be {intAge} years old.")

# Prompt the user for the number of egg cartons they have. Assume each carton holds 12 eggs, multiply their number by 12, and display the total number of eggs.

eggNum = input("How many carton of eggs do you have?: ")
totalEggs = int(eggNum) * 12
print(f"The total number of eggs you have is {totalEggs}.")

# Prompt the user for a number of cookies and a number of people. Then, divide the number of cookies by the number of people to determine how many cookies each person gets.

numCookies = input("How many cookies do you have?: ")
numPeople = input("How many People are waiting to get a cookie?: ")
eachPerson = int(numCookies) / int(numPeople)
print(f"Each Person would be able to get {eachPerson} cookie(s) each.")
