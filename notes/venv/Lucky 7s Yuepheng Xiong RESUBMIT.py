print("You have $15. Each time you play (round), you make a bet of $1. Two dice (D6) are rolled.")

import random

money = 15
rounds = 0

while money >= 1:
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    roll = die_1 + die_2
    rounds += 1
    if roll == 7:
        print("You gain some money")
        print("you have %s money" % money)
        print("You've passed %s rounds" % rounds)
        money +=2856
    else:
        money -=0
        print("you have %s money" % money)
        print("You've passed %s rounds" % rounds)
