
years = []
countries = []
life_expectancies = []

# Read data from the user
with open("life-expectancy2.csv") as csv_file:
    # Removes the heading of the file.
    heading = next(csv_file)

    for dataItem in csv_file:
        each = dataItem.split(",")
        country = each[0].strip()
        code = each[1].strip()
        year = each[2].strip()
        life_expectancy = each[3].strip()
        years.append(year)
        countries.append(country)
        life_expectancies.append(float(life_expectancy))

# Find the year and country with the lowest life expectancy
min_expectancy = min(life_expectancies)
min_index = life_expectancies.index(min_expectancy)
min_year = years[min_index]
min_country = countries[min_index]

# Find the year and country with the highest life expectancy
max_expectancy = max(life_expectancies)
max_index = life_expectancies.index(max_expectancy)
max_year = years[max_index]
max_country = countries[max_index]

# Allow the user to input a year
year_of_interest = input("Enter the year of interest: ")

# Find the overall max and min life expectancies
overall_max_year = max_year
overall_max_country = max_country
overall_min_year = min_year
overall_min_country = min_country

# Calculate the average life expectancy for the input year
year_data = [life_expectancies[i]
             for i in range(len(years)) if years[i] == year_of_interest]
average_life_expectancy = sum(year_data) / len(year_data)

# Find the country with the minimum and maximum life expectancies for the input year
min_expectancy = min(year_data)
min_index = year_data.index(min_expectancy)
min_expectancy_country = countries[min_index]

max_expectancy = max(year_data)
max_index = year_data.index(max_expectancy)
max_expectancy_country = countries[max_index]

# Print the results
print("The overall max life expectancy is:",
      overall_max_country, "in", overall_max_year)
print("The overall min life expectancy is:",
      overall_min_country, "in", overall_min_year)

print("\nFor the year", year_of_interest + ":")
print("The average life expectancy across all countries was",
      round(average_life_expectancy, 3))
print("The max life expectancy was in", max_expectancy_country,
      "with", round(max_expectancy, 3), "life expectancy")
print("The min life expectancy was in", min_expectancy_country,
      "with", round(min_expectancy, 3), "life expectancy")


# :::::::::::::::::::::::::::::: OLD CODE :::::::::::::::::::::::::::::::
# countries = []
# years = []
# code = []
# life_expectancy = []
# askUsers = ""
# max_life_expectancy = 0
# min_life_expectancy = 0
# overallMaxMessage = ""
# overallMinMessage = ""
# min_index = 0
# max_index = 0

# with open("life-expectancy2.csv") as csvFile:
#     # Removes the heading of the file.
#     heading = next(csvFile)

#     for dataItem in csvFile:
#         each = dataItem.split(",")
#         # print(each)
#         country = each[0].strip()
#         countries.append(country)
#         abrev = each[1].strip()
#         code.append(abrev)
#         year = each[2].strip()
#         years.append(year)
#         lifeExpectancy = each[3].strip()
#         life_expectancy.append(float(lifeExpectancy))
#         max_life_expectancy = max(life_expectancy)
#         min_life_expectancy = min(life_expectancy)
#         max_index = life_expectancy.index(max_life_expectancy)
#         min_index = life_expectancy.index(min_life_expectancy)
#         min_year = int(years[min_index])
#         min_country = countries[min_index]
#         max_year = int(years[max_index])
#         max_country = countries[max_index]

#     askUsers = input("Enter the year of interest: ")
#     print()
#     for i in life_expectancy:
#         # max_index = life_expectancy.index(max_life_expectancy)
#         # min_index = life_expectancy.index(min_life_expectancy)
#         if i == max_life_expectancy:
#             overallMaxMessage = (
#                 f"The overall max life expectancy is: {life_expectancy[max_index]} from {countries[max_index]} in {years[max_index]}")
#             # print(
#             #     f"The overall max life expectancy is: {i} from {countries[max_index]} in {years[max_index]}")
#             print(overallMaxMessage)
#         # if i == (min(life_expectancy)):
#         if i == min_life_expectancy:
#             overallMinMessage = (
#                 f"The overall min life expectancy is: {life_expectancy[min_index]} from {countries[min_index]} in {years[min_index]}")
#             # print(
#             #     f"The overall min life expectancy is: {i} from {countries[min_index]} in {years[min_index]}")
#             print(overallMinMessage)
#         # print(overallMaxMessage)
#     if askUsers in years:
#         for i in range(len(years)):
#             if years[i] == askUsers:
#                 # yearInfo = life_expectancy[i]
#                 print()
#                 print(f"For the year {askUsers}:")
#                 print(
#                     f"The average life expectancy across all countries was {sum(life_expectancy)/len(life_expectancy):.2f}")
#                 # print(
#                 # f"The max life expectancy was in {countries[i]} with {yearInfo:.2f}")
#                 print(
#                     f"The max life expectancy was in {countries[max_country]} with {life_expectancy[max_index]:.2f}")
# print(
#     f"The max life expectancy was in {countries[max_index]} with {life_expectancy[max_index]:.2f}")

# for i in years:
#     if i == askUsers:
# print(f"For the year {askUsers}:")
# print(
#     f"The average life expectancy across all countries was {sum(life_expectancy)/len(life_expectancy):.2f}")
# print(f"The max life expectancy was in {country} with {le:.2f}")
# print(f"The min life expectancy was in {country} with {le:.2f}")
