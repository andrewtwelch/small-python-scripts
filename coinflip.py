# Coin Flip

import random

#Return 0 or 1, 0 being heads and 1 being tails
def flipCoin():
    return random.randrange(0,2)

#Number Input with validation
def inputNumber(message):
    while True:
        try:
            number = int(input(message))
        except ValueError:
            print("Not an integer, please try again.")
            continue
        else:
            return number

flips = inputNumber("Enter the number of coin flips: ")
heads = 0
tails = 0

for x in range(0, flips):
    if flipCoin() == 0:
        heads += 1
        print("Heads!")
    else:
        tails += 1
        print("Tails!")

print("Final result:\nHeads = " + str(heads) + "\nTails = " + str(tails))
