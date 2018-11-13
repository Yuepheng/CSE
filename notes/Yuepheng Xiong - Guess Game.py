import random   # This should be on line 1
guesses = 5

random_number = random.randint(1, 10)

playing = True

while guesses > 0 and playing:
    guess = input("Guess a number from 0-10. You have five guesses")
    if int(guess) == int(random_number):
        print("You Win!")
        playing = False
    if int(guesses) > int(random_number):
        print("The number is too low.")
    if int(guesses) < int(random_number):
        print("The Number is too high")
    else:
        print("Try again")
        guesses = guesses - 1
