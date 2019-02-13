import string
import random
Punctuation = list(string.punctuation)
GameisOver = True
WordBank = ["Apple", "School", "Word", "Cat", "Run", "Notes",
            "Mad", "Can", "Fix", "Man", ]

word = random.choice(WordBank)
word_list = list(word)


letters_guessed = []
tries = 8


while tries > 0 and GameisOver:  # For when playing, This makes it to where if playing equals false, then it stops.
    hidden_word = []
    # Hide/SHow the word
    for letter in word:
        if letter in letters_guessed:
            hidden_word.append(letter)
        else:
            hidden_word.append("*")
    print(hidden_word)
    if "*" not in hidden_word:
        print("You Guessed all the letters correctly!")
        GameisOver = False

    print(hidden_word)

    guess = input("Type in a letter: ")  # UNDER THIS TEXT IS INFORMATIONAL STUFF
    letters_guessed.append(guess)

    tries -= 1

if not GameisOver:
    print("You Lost the Game")
