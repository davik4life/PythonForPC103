# Ask the user to enter a friends name

friends = []
requestFriendsName = ""
stopAsking = False

while not stopAsking:
    requestFriendsName = input("Type the name if a friend: ")
    if requestFriendsName.lower() != "end" and requestFriendsName != "":
        friends.append(requestFriendsName)
    else:
        print()
        print("Your friends are:")
        for friend in friends:
            print(friend)
        stopAsking = True
