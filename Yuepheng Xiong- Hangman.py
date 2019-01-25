import string
import random
Punctuation = list(string.punctuation)

WordBank = ["Apple.", "School.", "Word.", "Cat", "Run", "Notes",
            "Mad.", "Can.", "Fix.", "Man.", ]

word = random.choice(WordBank)
word_list = list(word)


letters_guessed = []
tries = 8


while tries > 0:
    hidden_word = []
    # Hide/SHow the word
    for letter in word:  # i goes through all indices
        if letter in letters_guessed:  # show the letter
            hidden_word.append(letter)
        else:
            hidden_word.append("*")
    print(hidden_word)

    guess = input("Type in a letter: ")  # UNDER THIS TEXT IS INFORMATIONAL STUFF
    letters_guessed.append(guess)

    tries -= 1
