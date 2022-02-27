#This is a game where you guess the number in a certain of amount of tries
#Difficulty ranges from Easy 1-10, Medium 1-50, and Hard 1-100

import random
###Assigning Variables
DifficultyLevels = {"easy", "medium", "hard", "impossible"}
name = ""
Difficulty = ""
TrueNumber = ""

###Creating Functions


def NewNumber():
    global TrueNumber 
    TrueNumber = random.randint(1,Difficulty)

def MainGame():
    print("Lets start playing! You only have 5 chances.")
    for Guesses in range(0,5):
        PlayerGuess = int(input("Choose a number between " + "1-" + str(Difficulty) + "\n"))

        if PlayerGuess < 1 or PlayerGuess > Difficulty:
            print("You didn't choose a number within the range.")
            MainGame()

        if PlayerGuess < TrueNumber:
            print("Too Low")
        elif PlayerGuess > TrueNumber:
            print("Too High")

        if PlayerGuess == TrueNumber:
            return 1
    print(TrueNumber)
    return 0
    
###Start of the game
print("Hello! I'm Rabbo The Rabbit. Welcome to my Guess The Number game.")


while name == "":
    name = input("Before we begin tell me your name?\n")

while Difficulty not in DifficultyLevels:
    try:
        Difficulty = str.lower(input(name + ", how hard do you want the game to be? Easy, Medium, Hard, Impossible\n"))
    except ValueError:
        print("Type a valid difficulty mode.")

match Difficulty:
    case "easy":
        Difficulty = 10
    case "medium":
        Difficulty = 50
    case "hard":
        Difficulty = 100
    case _:
        Difficulty = 1000000

print(name)
print(Difficulty)
NewNumber()
Status = MainGame()

if Status == 0:
    print("You lost")
else:
    print("You won")

