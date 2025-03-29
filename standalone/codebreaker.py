import random
# make the code
    # random.randint() x4 -> list[1,2,3,4]
# User tries to guess 4 digit code, computer gives you hint (each digit has to be within the range 1-9)
    # get the whole guess in one input -> then turn it to a list -> list("str")
# makw hint and print it out
    # make list hint
    # use if statements for each digit -> add approapiate letter to hint list for true if statement
    # the digit is in the right spot and is in the code = G(green)
    # the digit is in the code but not in the right spot= Y(yellow)
    # not in the code at all = R(Red)
    # [R,Y,G,G]
# user gets 5 attempts
    #each time the user guesses, its one attempt -> use a for else loop for this
# if you win, then its done
    # if hint is all "G"s, then its a win, then break
# if you lose, you can choose to do it again
    # handled by else in for else loop, ask user if they want to play again -> then run function again

code : list = []
for __ in range(4):
    digit : int = random.randint(1,9)
    code.append(digit)
print(code)


while True:
    userGuess : str = input("Enter your guess for the 4 digit number: ")
    try:
        int(userGuess)
    except ValueError as e:
        print("[ERROR] Not a number, try again")
        continue

    if len(userGuess) >= 5 or len(userGuess) < 4:
        print("[ERROR] Wrong length, try again")
        continue
    else:
        break

userGuessList = []
for c in userGuess:
    userGuessList.append(int(c))

hints = []
for index in range(len(userGuessList)):
    if userGuessList[index] == code[index]:
        hints.append("G")
    elif userGuessList[index] in code:
        hints.append("Y")
    else:
        hints.append("R")
print(hints)
