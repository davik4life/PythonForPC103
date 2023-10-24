# Receives a string and prints it out, exactly as received.
def display_regular(exact_string):
    print(exact_string)

# Receives a string, converts it to upper case, and then prints it out.


def display_uppercase(upper_case):
    message = upper_case.upper()
    print(message)

# Receives a string, converts it to lower case, and then prints it out


def display_lowercase(lower_case):
    message = lower_case.lower()
    print(message)


user_message = input("What is your message?")

display_regular(user_message)
display_uppercase(user_message)
display_lowercase(user_message)
