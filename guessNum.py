# 4、Guess the Number 

import random
number = random.randint(1,100)
print("The game is ready")

while True:
    guess = int(input("guess a number between 1 and 100 :"))
    if guess > number:
        print("higher")
    if guess < number:
        print("lower")
    if guess == number:
        print ("you guessed it")
        break
print("game is over")