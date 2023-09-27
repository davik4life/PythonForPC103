# Write a program to determine whether to loan money based on the following rules.

# First, ask for a rating from 1–10 on the following:

loanRating = float(input("On a Rating of 1 - 10, How large is the loan?: "))
creditHistoryRating = float(
    input("On a Rating of 1 - 10, How good is your credit history?: "))
incomeRating = float(
    input("On a Rating of 1 - 10, How high is your income?: "))
downPaymentRating = float(
    input("On a Rating of 1 - 10, How large is your down payment?: "))

# First, check if the loan size is at least 5. If it is, use the following rules: DONE
# If the credit history and income are both at least 7, then the decision is "yes" DONE
# If either the credit history or income is at least 7, then check if the down payment is at least 5, if it is, the decision is "yes", if not, the decision is "no" DONE
# Otherwise (if neither the credit history nor income is at least 7), the decision is "no" DONE
# ::::::  Otherwise (if the loan is not 5 or greater), use these rules:
# If the credit is less than 4, then the decision is "no"  DONE
# Otherwise, check the following:
# If either the income or the down payment is at least 7, the decision is "yes" DONE
# If both the income and the down payment are at least 4, then the answer is "yes" DONE
# Otherwise, the decision is "no" DONE

# Set the canAccessLoan to False by Default.
canAccessLoan = False

if loanRating >= 5:
    if creditHistoryRating >= 7 and incomeRating >= 7:
        canAccessLoan = True
    elif creditHistoryRating >= 7 or incomeRating >= 7:
        if downPaymentRating >= 5:
            canAccessLoan = True
        else:
            canAccessLoan = False
    else:
        canAccessLoan = False
elif creditHistoryRating < 4:
    canAccessLoan = False
elif incomeRating >= 7 or downPaymentRating >= 7:
    canAccessLoan = True
elif incomeRating >= 4 and downPaymentRating >= 4:
    canAccessLoan = True
else:
    canAccessLoan = False

# Display the decision to the user.
if canAccessLoan:
    print("Yes")
else:
    print("No")
