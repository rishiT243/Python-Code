#generate random sentence, with 5 words
    # setneces can be stored in a list
    # use random.choice()
import random

easySentences = ["Hello world", "Good morning", "Happy birthday", "Nice to meet you", "I love pizza", 
                 "Have a nice day", "See you soon", "Let's play", "Open the door", "Time for fun"]
mediumSentences = ["Practice makes perfect", "Better late than never", "Break a leg", "Speak of the devil",
                    "Keep your chin up", "Under the weather", "It's not rocket science", "Bite the bullet", 
                    "Hit the nail on the head", "Burning the midnight oil"]
hardSentences = ["Curiosity killed the cat", "A blessing in disguise", "Don't count your chickens", 
                 "A stitch in time saves nine", "Barking up the wrong tree", "Every cloud has a silver lining", 
                 "The ball is in your court", "Throw caution to the wind", "Caught between a rock and a hard place", 
                 "Steal someone's thunder"]

full="""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""

leg1="""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
"""

leg2 = """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
========="""

arm1 = """
  +---+
  |   |
  O   |
  |\\  |
      |
      |
========="""
arm2 = """
  +---+
  |   |
  O   |
  |   |
      |
      |
========="""

body = """
  +---+
  |   |
  O   |
      |
      |
      |
========="""

head = """
  +---+
  |   |
      |
      |
      |
      |
========="""

manHard = [head, body, full]
manMedium = [head, body, arm2, leg2, full]
manEasy = [head, body, arm2, arm1, leg2, leg1, full]

def hangman(man, sentences):
    currentMan = 0
    lettersUsed = []
    sentence = random.choice(sentences)
    notFilled = []
    for i in range(0,len(sentence)):
        if sentence[i] == " ":
            notFilled.append(" ")
        else:
            notFilled.append("_")

    firstLetter = sentence[0].lower()
    appearances = []
    for i in range(len(sentence)):
        if sentence[i].lower() == firstLetter:
            appearances.append(i)
    
    # go through each appearance and replace that spot in the not filled list with what it would be in the filled string
    for appearance in appearances:
        notFilled[appearance] = sentence[appearance]
    
    lettersUsed.append(firstLetter)


    while True:
        print(man[currentMan])
        if currentMan == len(man)-1:
            print("You lost!")
            break
        

        if "".join(notFilled).lower() == sentence.lower():
            print("You win!")
            break
        print("".join(notFilled))
        print()
        print("Letters used: " + ", ".join(lettersUsed))

        yn = input("Would you like to guess the sentence (y/n): ").lower()
        if yn == "y":
            guess = input("Enter your guess: ").lower()
            if guess != sentence.lower():
                currentMan += 1
                print("Nice try, your guess was wrong")
                continue
            else:
                print("You win!")
                break
        
        while True:
            letter = input("Enter a letter: ").lower()
            if len(letter) > 1:
                print("Put only one letter")
                continue
            elif letter in lettersUsed:
                print("letter already used")
                continue
            else:
                break
        # lettersUsed.append(letter)
        if letter not in sentence.lower():
            currentMan +=1
            print("This letter is not in the sentence.")
            lettersUsed.append(letter)
        else:
            # look through sentence one letter a time for matches
            appearances = []
            for i in range(len(sentence)):
                if sentence[i].lower() == letter:
                    appearances.append(i)
            
            # go through each appearance and replace that spot in the not filled list with what it would be in the filled string
            for appearance in appearances:
                notFilled[appearance] = sentence[appearance]
            
            lettersUsed.append(letter)


while True:
    options = """Options:
    E. Easy mode
    M. Medium mode
    H. Hard mode
    V. Very hard mode
    I. Impossible mode
    Q. Quit"""
    print(options)

    option = input("Enter an option: ").lower()
    if option == "e":
        hangman(manEasy, easySentences)
    elif option == "m":
        hangman(manMedium, easySentences)
    elif option == "h":
        hangman(manMedium, mediumSentences)
    elif option == "v":
        hangman(manMedium, hardSentences)
    elif option  == "i":
        hangman(manHard, hardSentences)
    elif option == "q":
        print("Thank you for playing!")
        break
    else:
        print("Invalid option, try again")
