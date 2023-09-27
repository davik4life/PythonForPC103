# Write a program that determines the letter grade for a course according to the following scale:

# A >= 90

# B >= 80

# C >= 70

# D >= 60

# F < 60


# Ask the user for their grade percentage, then write a series of if-elif-else statements
# to print out the appropriate letter grade. (At this point, you'll have a separate print statement
# for each grade letter in the appropriate block.) DONE

# Assume that you must have at least a 70 to pass the class. After determining the letter grade
# and printing it out. Add a separate if statement to determine if the user passed the course,
# and if so display a message to congratulate them. DONE
#
# If not, display a different message to encourage them for next time. DONE

# Change your code from the first part, so that instead of printing the letter grade in the body
# of each if, elif, or else block, instead create a new variable called letter and then in each block,
# set this variable to the appropriate value. Finally, after the whole series of if-elif-else
# statements, have a single print statement that prints the letter grade once.

letter = ""

gradePercentage = int(input("Enter your Grade Percentage: "))
if gradePercentage >= 90:
    letter = "A"
elif gradePercentage >= 80:
    letter = "B"
elif gradePercentage >= 70:
    letter = "C"
elif gradePercentage >= 60:
    letter = "D"
else:
    letter = "F"

print(f"Your Letter Grade is {letter}.")
passMark = False

if gradePercentage > 70:
    passMark = True

if passMark:
    print(
        f"Congratulation, You passed! You score is {gradePercentage}.")
else:
    print(
        f"Sorry, You did not pass. You may consider retaking the course. Your score is {gradePercentage}.")
