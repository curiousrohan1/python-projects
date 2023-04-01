import random
import array


def computeTitle(xp, games):
    if(xp/games >= 10):
        return "Psychic"
    elif(xp/games >= 7):
        return "Skilled"
    elif(xp/games >= 5):
        return "Experienced"
    elif(xp/games >= 3):
        return "Decent"
    elif(xp/games >= 0):
        return "Adequate"
    elif(xp/games >= -5):
        return "Beginner"
    else:
        return "Unfortunate"


def getXPChange(tries):
    if(tries == 0):
        return 10
    elif(tries <= 5):
        return 5
    elif(tries <= 7):
        return 3
    elif(tries <= 10):
        return 2
    else:
        return -5


def computeMax(maximum, xp):
    maximum += (xp*10)
    maximum = 10 * round(maximum/10)
    return maximum


def computeMin(minimum, xp):
    minimum -= (xp*10)
    minimum = 10 * round(minimum/10)
    return minimum


def getResponse(message):
    while(True):
        try:
            return int(input(message))
            break
        except ValueError as e:
            print(message)
            return 0


def rank(users):
    placeholder = dict({})
    for i in range(len(users)):
        for j in range(i):
            if((users[i]["xp"]/users[i]["games"]) > (users[j]["xp"]/users[j]["games"])):
                placeholder = users[j]
                users[j] = users[i]
                users[i] = placeholder
            elif((users[i]["xp"]/users[i]["games"]) == (users[j]["xp"]/users[j]["games"])):
                if((users[i]["maximum"]-users[i]["minimum"]) > (users[j]["maximum"]-users[j]["minimum"])):
                    placeholder = users[j]
                    users[j] = users[i]
                    users[i] = placeholder
                elif((users[i]["maximum"]-users[i]["minimum"]) == (users[j]["maximum"]-users[j]["minimum"])):
                    if(users[i]["tries"] < users[j]["tries"]):
                        placeholder = users[j]
                        users[j] = users[i]
                        users[i] = placeholder
    return users


def main():
    users = []
    users.append(dict({
        "title": "Beginner",
        "xp": 0,
        "minimum": 0,
        "maximum": 100,
        "games": 1,
        "username": input("Please input your name: "),
        "tries": 0
    }))
    i = 0
    while(True):
        user = users[i]
        print("\nYou are "+user["username"]+" the " +
              str(user.get("title"))+". This is game #"+str(user.get("games")) +
              ". You have "+str(user.get("xp"))+" points.\n")
        user["minimum"] = computeMin(user.get("minimum"), user.get("xp"))
        user["maximum"] = computeMax(user.get("maximum"), user.get("xp"))
        message = "Guess a price between " + \
            str(user.get("minimum"))+" and "+str(user.get("maximum"))+": "
        num_to_guess = random.randint(0, 100)
        tries = 0
        while(True):
            response = getResponse(message)
            if (response < user.get("minimum")):
                message = f"Whoops! {response} is below the minimum! Please try again: "
            elif (response > user.get("maximum")):
                message = f"Whoops! {response} is above the maximum! Please try again: "
            elif(response > int(num_to_guess)):
                message = f"{response} is greater than the number. Please try again: "
            elif(response < int(num_to_guess)):
                message = f"{response} is less than the number. Please try again: "
            else:
                print(
                    f"Congrats! You guessed it correctly in {tries+1} tries!")
                user["xp"] += getXPChange(tries)
                user["title"] = computeTitle(user.get("xp"), user.get("games"))
                user["tries"] += tries
                break
            tries = tries + 1
        user["games"] += 1
        if(input("Do you want to play again?(Y/n): ") == "n"):
            print("OK. Bye for now! xp was " +
                  str(user.get("xp"))+" points. The xp per game was "+str(user.get("xp")/(user.get("games")-1))+".")
            users[i] = user
            users = rank(users)
            print("Rankings:")
            for j in range(0, len(users)):
                print("    "+str(j+1)+"| "+users[j]["username"] + " the "+users[j]["title"]+"| "+str(users[j]["xp"])+" points| "+str(
                    users[j]["games"]-1)+" games| "+str(users[j]["maximum"]-users[j]["minimum"])+" maximum range| "+str(users[j]["tries"])+" tries|")
            break
        else:
            if(input("Is the same person playing?(Y/n): ") == "n"):
                users[i] = user
                username = input("Please input your name: ")
                foundIt = False
                for j in range(len(users)):
                    if(users[j]["username"] == username):
                        i = j
                        foundIt = True
                        break
                if(not foundIt):
                    i = len(users)
                    users.append(dict({
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
