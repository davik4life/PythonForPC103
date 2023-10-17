bonus = 1000
with open("hr_system.txt") as hrSystem:
    for eachData in hrSystem:
        organizedData = eachData.split()
        name = organizedData[0]
        idNumber = int(organizedData[1])
        jobTitle = organizedData[2]
        salary = float(organizedData[3])
        payCheck = salary / 24
        if jobTitle == "Engineer":
            payCheck += bonus
        print(f"{name} (ID: {idNumber}), {jobTitle} - ${payCheck:.2f}")
