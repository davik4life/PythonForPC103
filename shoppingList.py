items = []
askItems = ""
keepAsking = True
# count = 0
additionalItemsIndex = ""

# Loop through the items in the regular way (for example, for thing in the_list)
# and display each one to make sure you have the initial list built correctly.

# 1st Requirement. Begins :::Note: (Uncomment to be able to run the code.
# while keepAsking:
#     askItems = input(
#         "Please enter the items of the shopping list (type: quit to finish): ")
#     if askItems.lower() != "quit":
#         items.append(askItems)
#     else:
#         print()
#         for item in items:
#             print("Item: ", item)
#         keepAsking = False
# 1st Requirement. Ends

# 2nd Requirement Begins

# while keepAsking:
#     askItems = input(
#         "Please enter the items of the shopping list (type: quit to finish): ")
#     if askItems.lower() != "quit":
#         items.append(askItems)
#     else:
#         print()
#         print("The Shopping list is: ")
#         for item in items:
#             print(item)
#         keepAsking = False

# 2nd Requirement Ends

# 3rd Requirement Begins

while keepAsking:
    askItems = input(
        "Please enter the items of the shopping list (type: quit to finish): ")
    if askItems.lower() != "quit":
        items.append(askItems)
    else:
        print()
        print("The shopping list with indexes are: ")
        for i in range(len(items)):
            item = items[i]
            print(f"{i + 1}. {item}")
        # keepAsking = False
        print()
        additionalItemsIndex = int(
            input("Which item would you like to change? "))
        additionalItem = input("What is the new item? ")
        print()
        print("The shopping list with indexes are: ")
        for i in range(len(items)):
            items.pop(additionalItemsIndex - 1)
            items.append(additionalItem)
            item = items[i]
            print(f"{i + 1}. {item}")
            keepAsking = False
