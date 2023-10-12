# Ask for series of Numbers from the user.
numbers = []
keepAsking = True
sumOfNum = 0
averageNum = 0
largestNumber = 0

while keepAsking:
    numberEntries = int(
        input("Enter a list of numbers, type 0 when finished.: "))
    if numberEntries < 0:
        print("Only positive numbers are allowed.")
        break
    if numberEntries != 0:
        numbers.append(numberEntries)
        sumOfNum += numberEntries
        averageNum = sumOfNum / len(numbers)
    else:
        print()
        for number in numbers:
            if number > largestNumber:
                largestNumber = number
            print(f"Enter number: {number}")
        print(f"The sum is: {sumOfNum}")
        print(f"The average is: {averageNum}")
        print(f"The largest number is: {largestNumber}")
        keepAsking = False
