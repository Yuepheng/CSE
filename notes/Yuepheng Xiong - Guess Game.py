import random   # This should be on line 1

guess = input("Guess a number from 0-10")

random_number = random.randint(0, 10)

if int(guess) == int(random_number):
    print("You Win!")
else:
    print("Try again")
