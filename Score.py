import os
import os.path

def create_file():
    if os.path.isfile('Scores.txt'):
        print ("Keep playing")
    else:
        file = open('Scores.txt', 'w')
        file.write("0")
        file.close()

def score(difficulty):
    file = open('Scores.txt', 'r')
    current_score = file.read()
    print("Previous score: " + str(current_score))
    POINTS_OF_WINNING = (difficulty * 3) + 5
    print("You won: " + str(POINTS_OF_WINNING))
    new_score = int(current_score) + int(POINTS_OF_WINNING)
    print("new score is : " + str(new_score))
    file = open('Scores.txt', 'w')
    file.write(str(new_score))
    file.close()


create_file()
