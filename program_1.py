# Samuel Foss
# Program 1: Random dice
# 10/11/2024


# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).
# The dice sum will be the output of this function.
import random
MIN = 1
MAX = 6
start = 0


def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here
    number1 = random.randint(MIN, MAX)
    number2 = random.randint(MIN, MAX)
    # Sum 2 numbers
    number3 = number1 + number2
    # return sum to calling function
    return number3
for i in range(100):
    start += randDice()
start /= 100
print(f'{start:.2f}')
#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.

#output
#7.25

#Process finished with exit code 0
