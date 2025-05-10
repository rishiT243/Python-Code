#generate random sentence, with 5 words
    # setneces can be stored in a list
    # use random.choice()
import random

easySentences = ["Hello world", "Good morning", "Happy birthday", "Nice to meet you", "I love pizza", 
                 "Have a nice day", "See you soon", "Let’s play", "Open the door", "Time for fun"]
mediumSentences = ["Practice makes perfect", "Better late than never", "Break a leg", "Speak of the devil",
                    "Keep your chin up", "Under the weather", "It’s not rocket science", "Bite the bullet", 
                    "Hit the nail on the head", "Burning the midnight oil"]
hardSentences = ["Curiosity killed the cat", "A blessing in disguise", "Don’t count your chickens", 
                 "A stitch in time saves nine", "Barking up the wrong tree", "Every cloud has a silver lining", 
                 "The ball is in your court", "Throw caution to the wind", "Caught between a rock and a hard place", 
                 "Steal someone’s thunder"]

sentences = easySentences
lettersUsed = []


sentence = random.choice(sentences)
notFilled = []
# addNextLetter = False
for i in range(0,len(sentence)):
    # if addNextLetter == True:
    #     notFilled.append(sentence[i])
    #     addNextLetter = False
    #     continue
    if sentence[i] == " ":
        notFilled.append(" ")
        # addNextLetter = True
    else:
        notFilled.append("_")

# print(sentence)

full="""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""

legs = """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
========="""

arms = """
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

man = [full,legs,arms,body,head]

currentMan = 0

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


        
