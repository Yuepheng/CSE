import string
import random
Punctuation = list(string.punctuation)

WordBank = ["Apple.", "School.", "Word.", "Cat", "Run", "Notes",
            "Mad.", "Can.", "Fix.", "Man.", ]

word = random.choice(WordBank)
word_list = list(word)

tries = 8


while tries > 0:
    guess = input("Type in a letter: ")  # UNDER THIS TEXT IS INFORMATIONAL STUFF
    for i in range(len(WordBank)):  # i goes through all indices
        if word_list[] == "u":  # if we find a "U"
            word_list.pop()  # Remove the i-th index
            word_list.insert(, "*") # Put a * there instead
            print("You're Right")
        else:
            print("You're Wrong!")

tries -= 1
