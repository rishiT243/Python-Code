# generate a random number
    # num =random.randint(1,10) -> Integer
# have the user guess the number
    # g = input(eneter your guess) -> String
# if they're too low, tell them
    #if input < num -> print(too low)
# if they're too high, tell them
    # see above
# if they get it right, end the game, win
    #if g == num print(you win), end loop
# if the run out of attempts, end the game, lose
    #attempts = 5 
#for i in range(attempts)
    #game code
# else:
    #print you lose


# easy: 1-10, 5 attempts
# medium: 1-25, 5 attempts
# hard: 1-50, 5 attempts
# impossible: 1-100, 1 attempt

import random
# stores our valid inputs for exiting the game
no : list[str] = ["no", "n"]

# Generates a number that the user guesses depending on the # of attempts and the upper range of the generated number given as inputs
# returns an exit code: 0 -> Win, 1 -> Loss, 2 -> Quit
def guess_game(attempts : int, upper_range : int) -> int:
    # generates a random number between 1 and the given upper range
    num : int = random.randint(1,upper_range)

    # asks the user if they want to play or not
    # returns 2 if no, then quits
    # else continues with the game
    q : str= input("Do you want to play (y/n)?: ").lower()
    if q.lower() in no:
        return 2 # quit
    else:
        print("Have Fun!\n")

    # compares user guess to generated guess until out of attempts or the user guesses correctly
    # returns 0 on win, 1 on loss
    for i in range(attempts):

        # takes in user guess, and ensures input is valid (EX: within the guess range, and is a number)
        while True:
            g = 0
            while True:
                g = input(f"enter your number between 1 and {upper_range}: ")
                if not g.isdigit():
                    print("Invalid: Not a number or negative")
                    continue
                else:
                    break
            g = int(g)
            if g >  0 and g <= upper_range:
                break
            else:
                print("Invalid: Not in range")

        # outputs hints or correct guess statement to user
        if g < num:
            print("too low")
        elif g > num:
            print("too high")
        elif g == num:
            print("you win")
            return 0 # win
    else:
        print("You lose")
        return 1 # lose


# stores difficulties and their settings
# state : (attempts : str, upper_range : tuple(int,int))
states : dict = {
    "Easy" : (5, 10),
    "Medium": (5, 25),
    "Hard" : (5, 50),
    "Impossible" : (1, 100)
}

# stores our current state, initially set to easy
state : str = "Easy" # Medium, Hard, Impossible

# Runs our game and handles our state machine of difficulty modes
# game loop
while True:
    print(f"\nCurrent Gamemode: {state}")

    # passes our current state into our states dictionary to get the settings for that state
    # a_u = tuple(attempts , upper range)
    a_u : tuple = states[state]

    # those settings are then passed into our guess_game function
    result : int = guess_game(a_u[0], a_u[1])

    # if the user wants to quit the game (exit code 2), we end the game loop
    if result == 2: # Quit exit code
        print("Have good day!")
        break
    
    # Handles our state machine
    # Easy -win> medium -win> hard -win> impossible -win> game loop ends
    # when you lose you go back to the previous difficulty
    if state == "Easy":
        if result == 0: # Win exit code
            state = "Medium"
        elif result == 1: # Loss exit code
            continue
    elif state == "Medium":
        if result == 0: # Win exit code
            state = "Hard"
        elif result == 1: # Loss exit code
            state = "Easy"
    elif state == "Hard":
        if result == 0: # Win exit code
            state = "Impossible"
        elif result == 1: # Loss exit code
            state = "Medium"
    elif state == "Impossible":
        if result == 0: # Win exit code
            print("Congratulations, you beat impossible mode!!")
            break
        elif result == 1: # Loss exit code
            state = "Hard"
    else:
        # error handling for invalid state
        print("[ERROR] Invalid state")





