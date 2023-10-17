youngestAge = 99999999
youngestName = ""

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]


for ind in people:
    details = ind.split()
    name = details[0]
    age = int(details[1])
    if age < youngestAge:
        youngestAge = age
        youngestName = name
    print(f" {name} is {age} years old.")
print()
print(f"{youngestName} is the youngest, and his age is {youngestAge}")
