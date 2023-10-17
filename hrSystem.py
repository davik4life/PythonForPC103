

with open("hr_system.txt") as hrSystem:
    for eachData in hrSystem:
        organizedData = eachData.split()
        name = organizedData[0]
        idNumber = organizedData[1]
        jobTitle = organizedData[2]
        salary = organizedData[3]
        print(f"Name: {name}, Title: {jobTitle}")
