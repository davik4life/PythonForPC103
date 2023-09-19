# Write a program to convert from Fahrenheit to Celsius. Display the result to one decimal place of precision.

# To convert degrees in Fahrenheit to Celsius you need to subtract 32 from the Fahrenheit amount and then multiply it by the fraction 5/9.

convertToCelc = input("What is the temperature in Fahrenheit?: ")
intConvertToCacl = (float(convertToCelc) - 32) * 5/9
print(f"The temperature in Celsius is {intConvertToCacl:.1f} degrees.")
