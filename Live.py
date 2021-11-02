import time
from MainScores import *
from MemoryGame import *
from GuessGame import *
from CurrencyRouletteGame import *
from Score import *

def welcome():
    name = input("Hello, what's your name? ")
    print("Hello " + name + " and welcome to the World of Games (WOG)")


def load_game():
    print("""Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to
    guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS""")


def chosen_game():
    global game
    game = int(input("Which number do you choose? "))
    while game > 3 or game <= 0:
        print("You entered a wrong number!")
        print("please enter a number between 1 to 3: ")
        game = int(input("Which number do you choose? "))

    global difficulty
    difficulty = int(input("Please choose game difficulty from 1 to 5: "))
    while difficulty > 5 or difficulty <= 0:
        print("You entered a wrong number!")
        print("please enter a number between 1 to 5: ")
        difficulty = int(input("Which number do you choose? "))
        print(difficulty)
        return difficulty


welcome()
load_game()
chosen_game()


if game == 1:
    from MemoryGame import play
    win = play(difficulty)
    if win == True:
        score(difficulty)

elif game == 2:
    from GuessGame import play
    win = play(difficulty)
    if win == True:
        score(difficulty)

elif game == 3:
    from CurrencyRouletteGame import play
    win = play(difficulty)
    if win == True:
        score(difficulty)




create_file()
score(difficulty)
