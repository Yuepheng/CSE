import random
WordBank = ["Apple.", "School.", "Word.", "Cat", "Run", "Notes",
            "Mad.", "Can.", "Fix.", "Man.", ]

word = random.choice(WordBank)
word_list = list(word)

tries = 8

while tries > 0:
    guess = input("Type in a letter: ")


# CHANGE THIS LATER!!!
    tries -= 1
