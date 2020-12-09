from art import logo
import random
from replit import clear
clear()
print(logo)

#################################################### NUMBER GUESSING GAME ################################################################

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
number_chosen = random.randint(1,100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n")
if difficulty =='hard':
    lives = 5
else:
    lives = 10

print(f"You have {lives} attempts remaining to guess the number.")

while not lives == 0:
    guess = int(input("Make a guess : "))
    if guess==number_chosen:
        print("You guessed right")
        lives == 0
        break
    difference = number_chosen - guess
    if difference > 50:
        prompt ='very very low'
        lives -= 1
        print(f"You have {lives} attempts remaining to guess the number.")
    elif difference > 25:
        prompt ='too low'
        lives -= 1
        print(f"You have {lives} attempts remaining to guess the number.")
    elif difference > 10:
        prompt='low'
        lives -= 1
        print(f"You have {lives} attempts remaining to guess the number.")
    else:
        prompt='near'
        lives -= 1
        print(f"You have {lives} attempts remaining to guess the number.")
    if difference < 0:
        if difference > -50:
            prompt ='very very high'
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the number.")
        elif difference > -25:
            prompt ='too high'
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the number.")
        elif difference > -10:
            prompt='high'
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the number.")
        else:
            prompt='near'
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the number.")
    print(prompt)
