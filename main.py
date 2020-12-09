from art import logo
import random
from replit import clear


#################################################### NUMBER GUESSING GAME ################################################################

def number_generator(num):
    """Generates a random number between 1 and 100"""
    print(f"I am thinking of a number between 0 and {num+1}")
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
        
def game_start_screen_decor():
    clear()
    print(logo)
    print("Welcome to the Number Guessing Game!")

def game_start():
    """Main Game Function taking the max number"""
    # screen clearing and logo
    game_start_screen_decor()
    # game logic start
    max_number = int(input("Set the maximum number : "))
    # get difficulty
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n")
    # Generate a random number between 1 and max number
    number = number_generator(max_number)
    # Initialising lives(no of attempts)
    lives = lives_genertor(difficulty)
    
    while not lives == 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = guess_listener()
        lives = guess_verification(guess,number,lives)

    play_again=input("Do you want to play again ? \ny or n: ")
    if play_again=="y":
        return game_start()
    else:
        print("Thank you for playing the game\n - Samrood Ali")

    
# game launch
game_start()