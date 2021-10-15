import random

import logo

print(logo.logo)

print("Welcome to the Number Guessing Game!")
print("I'm of a number between 1 and 100.")

difficultyLevel = input("Choose a difficulty. Type 'easy' or 'hard' : ")

attempts = 0
if difficultyLevel == 'easy':
    attempts = 10
else:
    attempts = 5

number = random.randrange(1, 100)
while attempts > 0:
    print(f"You have {attempts} remaining to guss the answer")
    guess = int(input("Make a guess : "))
    if guess > number:
        print("Too high. \nguess again")
        attempts = attempts - 1
    elif guess < number:
        print("Too low. \nguess again")
        attempts = attempts - 1
    else:
        print("You win")
        break
