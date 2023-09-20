# Meal Calculator.

# Calculate the price of a child's meal
childsMeal = float(input("What is the price of a Child's meal?: "))
adultsMeal = float(input("What is the price of an Adult's meal?: "))
numOfChildren = int(input("How many children are there?: "))
numOfAdults = int(input("How many adult are there?: "))

# Break it down into reusable variables.
childMealsTotal = childsMeal * numOfChildren
adultMealsTotal = adultsMeal * numOfAdults

# Calculate the Sub Total
subTotal = childMealsTotal + adultMealsTotal
print()
print(f"Subtotal: ${subTotal:.2f}")
