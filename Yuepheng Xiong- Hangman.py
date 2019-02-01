import string
import random
Punctuation = list(string.punctuation)

WordBank = ["Apple.", "School.", "Word.", "Cat", "Run", "Notes",
            "Mad.", "Can.", "Fix.", "Man.", ]

word = random.choice(WordBank)
word_list = list(word)
word = "Apple"

letters_guessed = []
tries = 8

playing = True

while tries > 0:
    hidden_word = []
    # Hide/SHow the word
    for letter in word:
        if letter in letters_guessed:
            hidden_word.append(letter)
        else:
            hidden_word.append("*")
    for letter in word_list:
        if letter in word_list:
            playing = False
    print(hidden_word)

    guess = input("Type in a letter: ")  # UNDER THIS TEXT IS INFORMATIONAL STUFF
    letters_guessed.append(guess)

    tries -= 1

if not playing:
    playing = True

else:
    playing = False
