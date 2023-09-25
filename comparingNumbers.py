# Write a program that asks the user for two integers.

# Then, write three separate if/else statements as follows:

# If the first number is greater than the second, print "The first number is greater". Otherwise, print "The first number is not greater".

# If the two numbers are equal print "The numbers are equal". Otherwise, print "The numbers are not equal".

# If the second number is greater than the first, print "The second number is greater". Otherwise, print "The second number is not greater".
num1 = float(input("Enter the first Number: "))
num2 = float(input("Enter the second Number: "))
# num3 = float(input("Enter the third Number: "))

if num1 > num2:
    print("The first number is greater.")
else:
    print("The first number is not greater.")

if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal")

if num2 > num1:
    print("The second number is greater.")
else:
    print("The second number is not greater.")

print()
# Comparing Strings
# Have the program ask the user for their favorite animal. Then write an if statement as follows:

# Check to see if the user's favorite animal is the same as your favorite animal (meaning you, the programmer). If it is, print "That's my favorite animal too!" If it's not, print "That one is not my favorite." Verify that it works regardless of the capitalization.

favAnimal = input("What is your favorite animal?: ")

if favAnimal.capitalize() == "Dog":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")
