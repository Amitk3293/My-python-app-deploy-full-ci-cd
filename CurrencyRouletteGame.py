from currency_converter import CurrencyConverter
import random

c = CurrencyConverter('http://www.ecb.int/stats/eurofxref/eurofxref-hist.zip')
#difficulty = 3


def get_money_interval(difficulty):
    rate = int(c.convert(1, 'USD', 'ILS'))
    generate_usd = random.randint(1, 100)
    global t
    t = int(generate_usd) * rate
    interval = (t - (5 - difficulty), t + (5 - difficulty))
    print("How much are " + str(generate_usd) + "$ USD in ILS? ")
    return interval


def get_guess_from_user(difficulty):
    user_guess = input("What is your guess?: ")
    if user_guess == t:
        print("Awesome, you right! " + "The number is: " + str(t))
        print (int(user_guess))
        return True
    else:
        print("Please try again " + "The number is: " + str(t))
        return False

def play(difficulty):
    get_money_interval(difficulty)
    get_guess_from_user(difficulty)


# play(difficulty)
