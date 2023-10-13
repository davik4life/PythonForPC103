itemNames = ["Add item", "View cart", "Remove item", "Compute total", "Quit"]
itemPrice = 0
itemPrices = []
totalPrice = 0
cart = []
keepPlaying = True
selectItem = 0
addItem = ""
removeItem = 0
serialNum = 0
confirm = ""

print("Welcome to the Shopping Cart Program!")
print()

while keepPlaying:
    print()
    serialNum = 0
    print("Please select one of the following: ")
    for num, item in enumerate(itemNames, 1):
        print(f"{num}. {item}")
        # Ask the user for a number from the provided options.
    selectItem = int(input("Please select an action: "))
    # Add functionality to detect if the entered number is within range
    if selectItem in range(len(itemNames)):
        if selectItem == 1:
            addItem = input("What item would you like to add? ")
            itemPrice = float(input(f"What is the price of '{addItem}'? "))
            cart.append(addItem)
            itemPrices.append(itemPrice)
            print(f"'{addItem}' has been added to the cart.")
            continue
        elif selectItem == 2:
            print("The contents of the shopping cart are:")
            for i in range(len(cart)):
                serialNum += 1
                print(f"{serialNum}. {cart[i]} - ${itemPrices[i]:.2f}")
            continue
        elif selectItem == 3:
            removeItem = int(input("Which item would you like to remove? "))
            removeItem -= 1
            if removeItem in range(len(cart)):
                cart.pop(removeItem)
                itemPrices.pop(removeItem)
                print("Item removed")
            else:
                print(
                    "Sorry, that is not a valid item number.")
            continue
        elif selectItem == 4:
            totalPrice = sum(itemPrices)
            print(
                f"The total price of the items in the shopping cart is ${totalPrice:.2f}")
            continue

    elif selectItem == 5:
        print("Thank you. Goodbye.")
        keepPlaying = False
    else:
        print("Please ensure you have selected one of the numbers of each items presented to you.")
        print()
        print("Would you want to quit now and call back later or continue shopping?")
        confirm = input(
            "Enter 'QUIT' or any other letter to quit, or 'C' to continue.")
        if confirm.lower() == "quit":
            print("Thanks for shopping with us! Have a great day.")
            keepPlaying = False
        elif confirm.lower() == "c":
            keepPlaying = True
        else:
            keepPlaying = False
