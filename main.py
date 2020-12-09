from art import logo
import random
from replit import clear
clear()
print(logo)

#################################################### NUMBER GUESSING GAME ################################################################

print("Welcome to the Number Guessing Game!")

def number_generator(num):
    """Generates a random number between 1 and 100"""
    print(f"I am thinking of a number between 1 and {num}")
    number_chosen = random.randint(1,num)
    return number_chosen


def lives_genertor(difficulty):
    """Generates lives based on difficulty"""
    if difficulty =='hard':
        lives = 5
    else:
        lives = 10
    return lives


def guess_listener():
    guess = int(input("Make a guess: "))
    return guess

def guess_verification(guess,chosen_number,lives):
    if guess==chosen_number:
        print("You won")
        return 0
    elif lives > 1:
        lives -= 1
        if guess > chosen_number:
            print("too high")
        else:
            print("too low")
    else:
        print(f"Sorry,the number was {chosen_number}. You lose")
        return 0
    return lives
        

def game_start(num):
    """Main Game Function taking the max number"""
    
    # get difficulty
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n")
    # Generate a random number between 1 and num
    number = number_generator(num)
    # Initialising lives(no of attempts)
    lives = lives_genertor(difficulty)
    
    while not lives == 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = guess_listener()
        lives = guess_verification(guess,number,lives)

    # play_again=input("Do you want to ")
max_number = int(input("Set the maximum number : "))    
game_start(max_number)