## Collatz Conjecture

def inputNumber(message):
    while True:
        try:
            number = int(input(message))
        except ValueError:
            print("Not an integer, please try again.")
            continue
        else:
            return number

while True:
    number = inputNumber("Please enter a number above 1: ")
    if number <= 1:
        print("Number entered is less than or equal to 1. Please try again.")
        continue
    else:
        break

count = 0

while (number > 1):
    if (number % 2 == 1):
        oldnumber = number
        number *= 3
        number += 1
        count += 1
        number = int(number)
        print ("Step: " + str(count) + ": " + str(oldnumber) + " became " + str(number))
    else:
        oldnumber = number
        number /= 2
        count += 1
        number = int(number)
        print ("Step: " + str(count) + ": " + str(oldnumber) + " became " + str(number))


print("It took " + str(count) + " steps to get to 1.")