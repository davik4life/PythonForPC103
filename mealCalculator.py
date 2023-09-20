# Meal Calculator.
# I added the functionality to give a tip based on the actual amount and computed the calculation.
# I also used if else statement within my code to make it more simple and write a dry code.

# Calculate the price of a child's meal
childsMeal = float(input("What is the price of a Child's meal?: "))
adultsMeal = float(input("What is the price of an Adult's meal?: "))
numOfChildren = int(input("How many children are there?: "))
numOfAdults = int(input("How many adult are there?: "))
complimentary = "Thanks so much for your patronage. Have a nice day."

# Break it down into reusable variables.
childMealsTotal = childsMeal * numOfChildren
adultMealsTotal = adultsMeal * numOfAdults

# Calculate the Sub Total
subTotal = childMealsTotal + adultMealsTotal
print()
print(f"Subtotal: ${subTotal:.2f}")
print()

# What is the sales tax rate? Calculate it.

salesTaxRate = float(input("What is the sales tax rate?: "))
# Compute the Sales Tax with the Sub Total.
salesTax = subTotal * salesTaxRate / 100
total = subTotal + salesTax
print(f"Sales Tax: ${salesTax:.2f}.")
print(f"Total: ${total:.2f}.")
print()
# What is the payment amount? Calculate it.

paymentAmount = float(input("What is the payment amount?: "))
change = paymentAmount - total

# Ask the customer for a Tip
giveATip = input("Would you want to give a tip? (yes or no)")
# Code the conditions as needed.
if giveATip == "yes":
    getTip = float(input("Enter a Tip Amount: "))
    print(f"Thanks for giving a tip of ${getTip}.")
    newBalance = getTip + total
    print()
    print(f"Your new Total Fee is: ${newBalance:.2f}")
    newChange = paymentAmount - newBalance
    print()
    print(f"Change: ${newChange:.2f}.")
    print()
    print(complimentary)
else:
    print(f"Change: ${change:.2f}.")
    print()
    print(complimentary)
