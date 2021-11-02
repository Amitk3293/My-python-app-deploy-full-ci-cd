import random


# import Live


def generate_number(difficulty):
    global secret_number
    secret_number = int(random.randint(1, int(difficulty)))


def get_guess_from_user(difficulty):
    global guess
    guess = input("Please, guess a number between 1 to " + str(difficulty) + ": ")
    return guess


def compare_results():
    if secret_number == int(guess):
        print("Nice! you won the game")
        return True
    else:
        print("You didn't guess the number, please try again")
        print("The correct number is " + str(secret_number))
        return False


def play(difficulty):
    generate_number(difficulty)
    get_guess_from_user(difficulty)
    compare_results()

    if int(secret_number) == int(guess):
        print(True)
    else:
        print(False)
# play()
