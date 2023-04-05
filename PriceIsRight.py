import random


# Uses the average xp earned per game to assign a title to the player.
def compute_title(xp, games):
    if xp / games >= 10:
        return "Psychic"
    elif xp / games >= 7:
        return "Skilled"
    elif xp / games >= 5:
        return "Experienced"
    elif xp / games >= 3:
        return "Decent"
    elif xp / games >= 0:
        return "Adequate"
    elif xp / games >= -5:
        return "Beginner"
    else:
        return "Unfortunate"


# Calculates the number of points the player should gain after a game based on the number of tries it took them.
def getXPChange(tries):
    if tries == 0:
        return 10
    elif tries <= 5:
        return 5
    elif tries <= 7:
        return 3
    elif tries <= 10:
        return 2
    else:
        return -5


# Calculates the highest number in the range of the next game based on the points the user has.
def compute_max(maximum, xp):
    maximum += (xp * 10)
    maximum = 10 * round(maximum / 10)
    return maximum


# Calculates the lowest number in the range of the next game based on the points the user has.
def compute_min(minimum, xp):
    minimum -= (xp * 10)
    minimum = 10 * round(minimum / 10)
    return minimum


# Receives each number the user guesses in each game. If the user doesn't guess a number, the program tells them that
# it's not a valid value and prompts them once more.
def get_response(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("That's not a valid value.")


# Ranks all the players that have played the game so far.
def rank(users):
    dict({})
    for i in range(len(users)):
        for j in range(i):
            if (users[i]["xp"] / users[i]["games"]) > (users[j]["xp"] / users[j]["games"]):
                placeholder = users[j]
                users[j] = users[i]
                users[i] = placeholder
            elif (users[i]["xp"] / users[i]["games"]) == (users[j]["xp"] / users[j]["games"]):
                if (users[i]["maximum"] - users[i]["minimum"]) > (users[j]["maximum"] - users[j]["minimum"]):
                    placeholder = users[j]
                    users[j] = users[i]
                    users[i] = placeholder
                elif (users[i]["maximum"] - users[i]["minimum"]) == (users[j]["maximum"] - users[j]["minimum"]):
                    if users[i]["tries"] < users[j]["tries"]:
                        placeholder = users[j]
                        users[j] = users[i]
                        users[i] = placeholder
    return users


# The main function; begins the game and keeps track of all players.
def main():
    players = [dict({
        "title": "Beginner",
        "xp": 0,
        "minimum": 0,
        "maximum": 100,
        "games": 1,
        "username": input("Please input your name: "),
        "tries": 0
    })]
    i = 0
    while True:
        player = players[i]
        print("\nYou are " + player["username"] + " the " +
              str(player.get("title")) + ". This is game #" + str(player.get("games")) +
              ". You have " + str(player.get("xp")) + " points.\n")
        player["minimum"] = compute_min(player.get("minimum"), player.get("xp"))
        player["maximum"] = compute_max(player.get("maximum"), player.get("xp"))
        message = "Guess a price between " + \
                  str(player.get("minimum")) + " and " + str(player.get("maximum")) + ": "
        num_to_guess = random.randint(0, 100)
        tries = 0
        while True:
            response = get_response(message)
            if response < player.get("minimum"):
                message = f"Whoops! {response} is below the minimum! Please try again: "
            elif response > player.get("maximum"):
                message = f"Whoops! {response} is above the maximum! Please try again: "
            elif response > int(num_to_guess):
                message = f"{response} is greater than the number. Please try again: "
            elif response < int(num_to_guess):
                message = f"{response} is less than the number. Please try again: "
            else:
                print(
                    f"Congrats! You guessed it correctly in {tries + 1} tries!")
                player["xp"] += getXPChange(tries)
                player["title"] = compute_title(player.get("xp"), player.get("games"))
                player["tries"] += tries
                break
            tries = tries + 1
        player["games"] += 1
        if input("Do you want to play again?(Y/n): ") == "n":
            print("OK. Bye for now! xp was " +
                  str(player.get("xp")) + " points. The xp per game was " +
                  str(player.get("xp") / (player.get("games") - 1)) + ".")
            players[i] = player
            players = rank(players)
            print("Rankings:")
            for j in range(0, len(players)):
                print("    " + str(j + 1) + "| " + players[j]["username"] + " the " + players[j]["title"] + "| " + str(
                    players[j]["xp"]) +
                      " points| " + str(players[j]["games"] - 1) + " games| " + str(
                    players[j]["maximum"] - players[j]["minimum"]) +
                      " maximum range| " + str(players[j]["tries"]) + " tries|")
            break
        else:
            if input("Is the same person playing?(Y/n): ") == "n":
                players[i] = player
                username = input("Please input your name: ")
                found_it = False
                for j in range(len(players)):
                    if players[j]["username"] == username:
                        i = j
                        found_it = True
                        break
                if not found_it:
                    i = len(players)
                    players.append(dict({
                        "title": "Beginner",
                        "xp": 0,
                        "minimum": 0,
                        "maximum": 100,
                        "games": 1,
                        "username": username,
                        "tries": 0
                    }))
            print("Okay! Get ready!")


main()
