from art import logo
import random
from replit import clear
print(logo)

#################################################### NUMBER GUESSING GAME ################################################################

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
number_chosen = random.randint(1,100)
print("Psst,the correct number is :",number_chosen)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': hard")
if difficulty =='hard':
    lives = 5
else:
    lives = 10