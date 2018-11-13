print("You have $15. Each time you play (round), you make a bet of $1. Two dice (D6) are rolled.")

import random
die_1 = random.randint(1, 6)
die_2 = random.randint(1, 6)
money = 15
rounds = 0

while money > 0:
    if die_1 + die_2 == 7:
