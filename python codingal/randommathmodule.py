import random
playing=True
number=str(random.randint(0,9))
print("It will generate a number from 0-9 and you have to guess it.")
print("The game ends when you get the number correct.")
while playing:
    guess=input("Guess the number:")
    if number==guess:
        print("You win the game")
        print("The number was",number)
        break
    else:
        print("The number is wrong.")

import math
print("The Floor and Ceiling value of 23.56 are "+str(math.floor(23.56))+" "+str(math.ceil(23.56)))

x=10
y=-15
print("The value of x after copying the sign from y is "+str(math.copysign(x,y)))

print("The absolute value of -96 and 56 is "+str(math.fabs(-96))+" "+str(math.fabs(56)))

print("The GCD of 24 and 56 is "+str(math.gcd(24,56)))