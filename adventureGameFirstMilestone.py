# This is the First Milestone for the week. I also created a design using a diagram tool.
# before implementing on VSCode.

# Setup three variables as a place holder for the three possible choices throughout the game.
choice1 = ""
choice2 = ""
choice3 = ""
firstQuest = ""
secQuest = ""
thirdQuest = ""

# My adventure game is based on a Young Member of The Church of Jesus Christ of Latter-Day
# Saints, struggling to make a decision to either go to the University and ignore serving a Full-Time
# Mission, or first go on a Mission and then continue his education after his return.

print("Welcome to the Adventure Game!!! \n")
print("____________________________________")
print()
print("You would be presented with a set of questions")
print()
print("You are to use the provided keywords to play the game")
print("____________________________________")
print()

firstQuest = input("You just turned 18, and you have the desire to go serve a fulltime mission. You also have to go to school but you can always choose to continue your education after your return from mission. Which would you choose? Enter either the word 'SERVE' or 'SCHOOL': ")
choice1 = firstQuest.upper()
if choice1 == "SERVE":
    print()
    print(
        f"Awesome!!! You have chosen to '{choice1}' The Lord on a Full-Time Mission.")
    print()
    secQuest = input(
        "If given the chance a continent to serve, which of these two would you choose? 'AFRICA' or 'ASIA'")
    choice2 = secQuest.upper()
    if choice2 == "AFRICA":
        print()
        thirdQuest = input(
            f"Where in '{choice2}' would you want to Serve? 'SOUTH-AFRICA' or 'WEST-AFRICA'?: ")
        choice3 = thirdQuest.upper()
        if choice3 == "SOUTH-AFRICA":
            print()
            print(
                f"{choice3} is such a beautiful place. We do hope you will give your best in The Lord's work.")
            print("Thanks for playing this Adventure Game.")
        elif choice3 == "WEST-AFRICA":
            print()
            print(
                f"{choice3} is a group of countries in the West-African region.")
            print(
                "So many countries to choose from, Nigeria, and Ghana are some of the popular picks. Enjoy Your Mission.")
        else:
            print("You have entered a wrong keyword")
            print("To play this game, the keywords have to be exact.")
    elif choice2 == "ASIA":
        print()
        thirdQuest = input(
            f"Where in '{choice2}' would you want to Serve?: ''VIETNAM' or 'SINGAPORE': ")
        choice3 = thirdQuest.upper()
        print()
        if choice3 == "VIETNAM":
            print()
            print(
                f"{choice3} is such a beautiful place, and is rated one of the best places to visit in Asia.")
            print()
            print(
                "Awesome pick!!! At the end of it all, You will go whereever The Lord would ask you to go.")
        elif choice3 == "SINGAPORE":
            print()
            print(
                f"Great place to Serve. {choice3} is known to be a place of Peace. Singaporeans are peaceful people.")
            print("Thanks for playing this game.")
        else:
            print("You have entered a wrong keyword")
            print("To play this game, the keywords have to be exact.")
    else:
        print("You entered the wrong input. To play this game, you must follow the set guidlines.")
elif choice1 == "SCHOOL":
    print()
    print(
        f"You chose {choice1}, and we do hope you are making the right choice.")
    print()
    secQuest = input(
        "Do you believe Serving a Full-Time Mission is a Commandment from our Heavenly Father?: Answer with a 'YES', 'NO': ")
    choice2 = secQuest.upper()
    if choice2 == "YES":
        print()
        thirdQuest = input(
            "Would you want to counsel with your Bishop or your local church leaders to help guide you on what to do? 'YES' or 'NO' or 'NOT SURE': ")
        choice3 = thirdQuest.upper()
        if choice3 == "YES":
            print()
            print("Great idea! Pls schedule a time with your Bishop or local church leaders and you will be able to know what Heavenly Father would have you do at this time.")
        elif choice3 == "NO" or choice3 == "NOT SURE":
            print()
            print(
                "Okay, Take some time to pray and study the scriptures to be guided.")
        else:
            print()
            print("You have entered the wrong details, pls follow the set of instructions given to be able to play this game. Thanks.")
    elif choice2 == "NO":
        print()
        print("Serving a Full-Time Mission is a commandment from Heavenly Father, and He wants us to spread the gospel to all Nations.")
        print()
        secQuest = input(
            "Would you be happy if you got a guidance from a Bishop of a local church leader? 'YES' or 'NO': ")
        choice3 = secQuest.upper()
        if choice3 == "YES":
            print()
            print(f"{choice3}!!! You have made the right choice. Take out time to meet with a church leader and also pray about your decision.")
        elif choice3 == "NO":
            print()
            print("Take sometime to read the 'PREACH MY GOSPEL' manual within the Gospel Library. It would also help clarify why it is important to serve a mission.")
        else:
            print()
            print("You have entered a wrong input.")
    else:
        print(
            "You have entered the wrond input, try to adhere to the rules of the game.")
else:
    print("You had a wrong entry. Pls try follow the game instructions.")
