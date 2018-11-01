import random   # This should be on line 1

print("Guess a number from 0-10")

random_number = random.randint(0, 10)

guess_1 = input("Guess #1")
print("The Answer %s is Incorrect" % guess_1)
