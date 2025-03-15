import random

# player vs com
# we need to get the player choice and the robot choice for rock paper or scissors
    # how to get player choice: input("question: ") then save that to a variable (make sure its rock paper or scissors)
    # how to get the robot choice: random module, choice() on a list [done]
# we need to figure out who beats who
# declare a winner
# keep playing

choices = ["Rock", "Paper", "Scissors"]
wins = 0
losses = 0
draws = 0
gameOver = False
start = True
while not gameOver:
    if not start:
        print()
        print("------------------------------------------------")
        answer = input("Do you want to keep playing? (y/n): ")
        answer = answer.lower()
        if answer == "n" or answer == "no":
            print("Goodbye!")
            gameOver = True
            break
        elif answer == "yes" or answer == "y":
            pass
        else:
            print("I'm going to assume you want to keep playing")
        
    # randomly picks robot choice
    robot = random.choice(choices) 

    # asks the user to pick a choice, and makes sure it is correct
    while True:
        player = input("Choose Rock, Paper, or Scissors: ")
        player = player.capitalize()
        if not player in choices:
            continue
        else:
            break

    # displays choices
    print(f"Player Choice: {player}")
    print(f"Robot Choice: {robot}")

    # displays results
    if(player == robot):
        draws += 1
        print("Draw")
        print(f"Wins: {wins}")
        print(f"Losses: {losses}")
        print(f"Draws: {draws}")
    elif (player == "Rock" and robot == "Scissors") or (player == "Scissors" and robot == "Paper") or (player == "Paper" and robot == "Rock"):
        wins += 1
        print("You win")
        print(f"Wins: {wins}")
        print(f"Losses: {losses}")
        print(f"Draws: {draws}")
    else:
        losses += 1
        print("You lose")
        print(f"Wins: {wins}")
        print(f"Losses: {losses}")
        print(f"Draws: {draws}")
    start = False
