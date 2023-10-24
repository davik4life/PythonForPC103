# ask_users_input()

ask_user = float(input("What is the temperature? "))
fah_or_calc = input("Fahrenheit or Celsius (F/C)? ")

# function that converts the inputed data to Celsius


def converter():
    conv = (ask_user * 9/5) + 32
    return conv


def check_temp():
    if fah_or_calc.upper() == "F":
        for i in range(5, 61, 5):
            calci_fah = 35.74 + (0.6215 * ask_user) - 35.75 * \
                (i ** 0.16) + 0.4275 * ask_user * (i ** 0.16)
            print(
                f"At temperature {ask_user}F, and wind speed {i} mph, the windchill is: {calci_fah:.2f}F")
        return

    elif fah_or_calc.upper() == "C":
        converted = converter()
        for i in range(5, 61, 5):
            calci_cel = 35.74 + (0.6215 * converted) - 35.75 * \
                (i ** 0.16) + 0.4275 * converted * (i ** 0.16)
            print(
                f"At temperature {converted}F, and wind speed {i} mph, the windchill is: {calci_cel:.2f}F")
        return


check_temp()
