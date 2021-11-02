import time
import random
import os

#difficulty = 3


def generate_sequence(difficulty):
    input("The number will be displayed for 0.7 seconds, press Enter to continue")
    global random_numbers
    random_numbers = []
    for num in range(int(difficulty)):
        random_numbers.append(random.randrange(1, 101))
    print(random_numbers)
    time.sleep(0.7)
    os.system('clear')
    return random_numbers


def get_list_from_user(difficulty):
    input("Are you ready to guess the numbers?, press Enter to continue")
    global user_list
    user_list = []
    for num in range(0, difficulty):
        user_num = int(input("Please fill in each number and press Enter: "))
        user_list.append(user_num)
    print("Your chosen numbers are : " + str(user_list))
    return user_list


def is_list_equal(difficulty):
    if user_list == random_numbers:
        print("Cool, you guess all the numbers")
        return True
    else:
        print("You didn't guess the numbers, you can try again")
        return False


def play(difficulty):
    generate_sequence(difficulty)
    get_list_from_user(difficulty)
    is_list_equal(difficulty)
    if user_list == random_numbers:
        return(True)
    else:
        return(False)



# play()