from art import logo
import random

EASY_MODE_LIVES = 10
HARD_MODE_LIVES = 5

#Function for easy mode lives
def easyModeLives():
    return EASY_MODE_LIVES

#Function for hard mode lives
def hardModeLives():
    return HARD_MODE_LIVES

#Function for conditions

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking a number between 1 and 100")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        lives = easyModeLives()
        print(f"You've chosen easy mode, you have {lives} lives")
    else:
        lives = hardModeLives()
        print(f"You've chosen hard mode, you have {lives} lives")

#Function for random number
    machineNum = random.randint(1, 101)
    game_continue = True
    while game_continue:
        numGuess = input("Guess a number: ")
        if int(numGuess) > int(machineNum):
            lives = lives - 1
            print(f"Too high! You have {lives} left. Try another number")
            if lives == 0:
                game_continue = False
                print(f"You have {lives} lives left, Sorry you lost! The correct answer was {machineNum}")
                play_again = input("Do you want to play again? Yes or No? ")
                if play_again == 'Yes':
                    play_game()
        elif int(numGuess) < int(machineNum):
            lives = lives - 1
            print(f"Too low! You have {lives} left. Try another number")
            if lives == 0:
                game_continue = False
                print(f"You have {lives} left. Sorry you lost! The correct answer was {machineNum}")
                play_again = input("Do you want to play again? Yes or No? ")
                if play_again == 'Yes':
                    play_game()
        elif int(numGuess) == int(machineNum):
            print(f"Congrats you got the right number, YOU WON! The number was {machineNum}")
            game_continue = False
            play_again = input("Do you want to play again? Yes or No? ")
            if play_again == 'Yes':
                play_game()
            else:
                game_continue = False


play_game()




