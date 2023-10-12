# Ask for series of Numbers from the user.
numbers = []
keepAsking = True
sumOfNum = 0
averageNum = 0
largestNumber = 0
smallestNumber = 999999999

while keepAsking:
    numberEntries = int(
        input("Enter a list of numbers, type 0 when finished.: "))
    if numberEntries != 0:
        numbers.append(numberEntries)
        sumOfNum += numberEntries
        averageNum = sumOfNum / len(numbers)
    else:
        print()
        for number in numbers:
            if number > largestNumber:
                largestNumber = number
            if number > 0 and number < smallestNumber:
                smallestNumber = number
            print(f"Enter number: {number}")
        print(f"The sum is: {sumOfNum}")
        print(f"The average is: {averageNum}")
        print(f"The largest number is: {largestNumber}")
        print(f"The smallest positive number is: {smallestNumber}")
        print("The sorted list is:")
        for i in sorted(numbers):
            print(i)
        keepAsking = False
