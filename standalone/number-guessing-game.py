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
yes = ["yes", "y", "ok"]
no = ["no", "n"]

def guess_game(attempts, upper_range):
    num = random.randint(1,upper_range)
    q = input("Do you want to play (y/n)?: ").lower()
    if q in no:
        return "Quit"
    else:
        print("Have Fun!\n")
    for i in range(attempts):
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

        if g < num:
            print("too low")
        elif g > num:
            print("too high")
        elif g == num:
            print("you win")
            return True # win
    else:
        print("You lose")
        return False

# guess game is gonna return true on win, false on loss
# state : (attempts, upper_range)
states = {
    "Easy" : (5, 10)
}
state = "Easy" # Meidum, Hard, Impossible

a_u = states[state]
result = guess_game(a_u[0], a_u[1])




