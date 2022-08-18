import os
import random
from random_word import RandomWords


def clearTerminal():
    """
    Clears the terminal
    """
    os.system('cls||clear')


def validateData(valid_values):
    """
    check of the value entered by user is valid
    """
    while True:
        try:
            value = input()
            if value not in valid_values:
                raise ValueError(f"Please enter a value between {valid_values}")
            else:
                return value
        except ValueError as error:
            print(f"Invalid data: {error}, please try again.\n")


def runRPS():
    """
    This function is the Rock, Paper, Scissors Game
    """
    choices = ["Rock", "Paper", "Scissors"]
    user_score = 0
    computer_score = 0

    while True:
        print(" 1 : Rock \n 2 : Paper\n 3 : Scissors")
        print("Please choose 1, 2, 3 or enter # to exit:")
        choice = validateData(['1', '2', '3', '#'])
        
        clearTerminal()
        if choice == '1':
            user_choice = 'Rock'
        elif choice == '2':
            user_choice = 'Paper'
        elif choice == '3':
            user_choice = 'Scissors'
        else:
            print(f"your final score:     {user_score}") 
            print(f"computer final score: {computer_score}\n") 
            print("Thanks for playing\n")    
            main() 

        computer_choice = random.choice(choices)
        if user_choice == computer_choice:
            # just to reduce the posibility of same choices
            computer_choice = random.choice(choices)
        print(f"you:     {user_choice} \ncomputer: {computer_choice} \n")

        if user_choice == computer_choice:
            print("it's a tie game!")
        elif user_choice == "Rock":
            if computer_choice == "Paper":
                print("you lost!")
                computer_score = increaseScore(1, computer_score)

            if computer_choice == "Scissors":
                print("you won!")
                user_score = increaseScore(1, user_score)

        elif user_choice == "Scissors":
            if computer_choice == "Rock":
                print("you lost!")
                computer_score = increaseScore(1, computer_score)

            if computer_choice == "Paper":
                print("you won!")
                user_score = increaseScore(1, user_score)

        elif user_choice == "Paper":
            if computer_choice == "Rock":
                print("you won!")
                user_score = increaseScore(1, user_score)

            if computer_choice == "Scissors":
                print("you lost!")
                computer_score = increaseScore(1, computer_score)
        print(f"your score:     {user_score} ")
        print(f"computer score: {computer_score}\n")
         

def increaseScore(scoreToAdd, mainScore):
    """ function to increase the mainScore by scoreTo Add"""

    mainScore += scoreToAdd
    return mainScore


def runGTW(score):
    """
    This function provide list of alphabets to user and user shpuld guess 
    the word
    """
    clearTerminal()
    print("1 : Easy    | every win 1 score")
    print("2 : Medium  | every win 2 score")
    print("3 : Hard    | every win 3 score")
    
    print("Please select the level of the game or # to exit")
    level = validateData(['1', '2', '3', '#'])
    if level == '#':
        print("Thank you for playing")
        main()

    print("Guess the word with all following letters.")
    r = RandomWords()
    word = ""
    if level == '1':
        word = r.get_random_word(hasDictionaryDef="true", minLength=2, maxLength=5)
    elif level == '2':
        word = r.get_random_word(hasDictionaryDef="true", minLength=5, maxLength=7)
    elif level == '3':
        word = r.get_random_word(hasDictionaryDef="true", minLength=7)
    
    letters = [x for x in word]
    random.shuffle(letters)
    print(letters)
    user_guess = input()
    if user_guess.lower() == word.lower():
        print("Good job, you found the word")
        score = increaseScore(int(level), score)
        print(f'score: {score}')
    else:
        print(f"{user_guess} is not the right answer, it's {word}")
        print(f'score: {score}')

    print("Enter * to continue or # to exit")
    a = validateData(['#', '*'])
    if a == '*':
        runGTW(score)
    elif a == '#':
        main()
    

def main():
    """
    Main program functions
    """
    print("Lets select which game you wanna play")
    print("Enter 1 for  Rock, Paper, Scissors!")
    print("Enter 2 for guess the word!")
    print("Enter # to exit")
    games = ['1', '2', '#']
    game = validateData(games)
  
    if game == '1':
        clearTerminal()
        print("You selected Rock, Paper, Scissors. Good Luck!\n")
        runRPS()
    elif game == '2':
        clearTerminal()
        print("You selected guess the word. Good Luck!\n")
        runGTW(0)
    else:
        print("Thank you for playing")
        exit()


print("Welcome, Lets have some fan today!")
main()
# https://cloud.smartdraw.com/?nsu=1


