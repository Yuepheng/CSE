import string
import random
Punctuation = list(string.punctuation)

WordBank = ["Apple.", "School.", "Word.", "Cat", "Run", "Notes",
            "Mad.", "Can.", "Fix.", "Man.", ]

word = random.choice(WordBank)
word_list = list(word)

tries = 8


while tries > 0:
    guess = input("Type in a letter: ")
    if guess == list(word):
        WordBank.pop(20)
        WordBank.insert(, ""):

        tries -= 1
