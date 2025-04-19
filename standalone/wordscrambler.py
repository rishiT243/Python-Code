import random
while True:
    a = input("do you want to play (y/n): ").lower()
    if a == "y":
        words = ["python", "coder", "word", "apple", "banana", "cherry", "dog", "elephant", "guitar", "house", "ink", "jump", "kite", "lemon", 
                "mountain", "night", "orange", "piano", "quilt", "rose", "sunflower", "tree", "umbrella", "violet", "water", "xylophone", "yellow", 
                "zebra", "ball", "cake", "dolphin", "eggplant", "flame", "grape", "hammer", "ice", "jungle", "koala", "lion", "mango", "nectar", 
                "ocean", "penguin", "quicksand", "rocket", "star", "tiger", "unicorn", "vulture", "whale", "x-ray", "yoga", "zoo", "airplane", "boat", 
                "cat", "doghouse", "elephant", "forest", "green", "hill", "igloo", "jackal", "key", "lake", "mountain", "nightmare", "octopus", "parrot",
                "queen", "rosebud", "seashell", "treehouse", "umbrella", "volcano", "window", "yellowstone", "zigzag", "awesome", "bicycle", "cloud", 
                "drum", "earth", "flower", "grass", "hilltop", "island", "jellyfish", "kingdom", "lighthouse", "moss", "nature", "owl", "pyramid", 
                "quasar", "rainbow", "sun", "turtle", "universe", "vine", "whisper", "xenon", "yarn", "zigzag"]
        word = random.choice(words)
        while True:
            original = word
            word = list(word)
            random.shuffle(word)
            word = "".join(word)
            if word == original:
                continue
            else:
                break
        print(word)
        for i in range(5):
            print(f"Attempts left: {5 - i}")
            b = input("enter your guess for the unscrambled word: ")
            if b == original:
                print("You win!")
                break
            else:
                print("Try again")
        else:
            print("You lose!")
    else:
        print("Goodbye!")
        break


# Data types:
    # Integers -> whole numbers and their opposites
    # Strings -> "text"
    # Booleans -> True or False
    # Floats -> decimal numbers and their opposites

# Operators
    # Arithmetic: +,*,-,/,**,%,//
    # Comparison: ==, >,<, >=, <=, !=
    # Logical: not (!), and (&&), or (||)


# True and True -> True
# True and False -> False
# False and False -> False

# True or False -> True
# False or False -> False
# True or True -> True

# not False -> True

# not False and True or False -> True
