years = []
countries = []
life_expectancies = []


# Read data from the user
with open("life-expectancy.csv") as csv_file:
    # Removes the heading of the file.
    heading = next(csv_file)

    # I will now iterate over all the data and make a copy into the list and then analyse
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
print()

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
min_index = life_expectancies.index(min_expectancy)
min_expectancy_country = countries[min_index]

max_expectancy = max(year_data)
max_index = life_expectancies.index(max_expectancy)
max_expectancy_country = countries[max_index]

print("The overall max life expectancy is:", max(life_expectancies),
      "from", overall_max_country, "in", overall_max_year)
print("The overall min life expectancy is:", min(life_expectancies),
      "from", overall_min_country, "in", overall_min_year)

print("\nFor the year", year_of_interest + ":")
print("The average life expectancy across all countries was",
      round(average_life_expectancy, 2))
print("The max life expectancy was in", max_expectancy_country,
      "with", round(max_expectancy, 3))
print("The min life expectancy was in", min_expectancy_country,
      "with", round(min_expectancy, 3))
