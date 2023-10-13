itemName = ""
itemNames = ["Add item", "View cart", "Remove item", "Compute total", "Quit"]
itemPrice = 0
itemPrices = []
cond = "quit"
cart = []
keepPlaying = True
selectItem = 0
addItem = ""

print("Welcome to the Shopping Cart Program!")

while keepPlaying:
    print()
    print("Please select one of the following: ")
    for num, item in enumerate(itemNames, 1):
        print(f"{num}. {item}")
    selectItem = int(input("Please enter an action: "))
    # Add functionality to detect if the entered number is within range
    if selectItem in range(len(itemNames)):
        if selectItem == 1:
            addItem = input("What item would you like to add? ")
            cart.append(addItem)
            print(f"'{addItem}' has been added to the cart.")
            continue
        elif selectItem == 2:
            print("The contents of the shopping cart are:")
            for i in cart:
                print(i)
            continue
    elif selectItem == 5:
        print("Thank you. Goodbye.")
        keepPlaying = False
