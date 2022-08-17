import random
from random_word import RandomWords
import os


def clearTerminal():
    """
    Clears the terminal
    """
    os.system('cls||clear')


def runRPS():
    """
    This function is the Rock, Paper, Scissors Game
    """
    choices = ["Rock", "Paper", "Scissors"]
    user_score = 0
    computer_score = 0
    contin = True

    while contin is True:
        while True:
            print(" 1 : Rock \n 2 : Paper\n 3 : Scissors")
            choice = input("Please choose 1, 2, 3 or enter e to exit:\n")
            clearTerminal()
            if choice == '1':
                user_choice = 'Rock'
                break
            elif choice == '2':
                user_choice = 'Paper'
                break
            elif choice == '3':
                user_choice = 'Scissors'
                break
            elif choice.lower() == 'e':
                contin = False
                clearTerminal()
                break
            else:
                print("You entered envalid value\n")

        computer_choice = random.choice(choices)
        print(f"you:     {user_choice} \ncomputer: {computer_choice} \n")

        if user_choice == computer_choice:
            print("it's a tie game!")
        elif user_choice == "Rock":
            if computer_choice == "Paper":
                print("you lost!")
                computer_score += 1

            if computer_choice == "Scissors":
                print("you won!")
                user_score += 1

        elif user_choice == "Scissors":
            if computer_choice == "Rock":
                print("you lost!")
                computer_score += 1

            if computer_choice == "Paper":
                print("you won!")
                user_score += 1

        elif user_choice == "Paper":
            if computer_choice == "Rock":
                print("you won!")
                user_score += 1

            if computer_choice == "Scissors":
                print("you lost!")
                computer_score += 1
        print(f"your score:     {user_score} ")
        print(f"computer score: {computer_score}\n")

    print(f"your final score:     {user_score}") 
    print(f"computer final score: {computer_score}\n") 
    print("Thanks for playing\n")    
    main()       


def increaseScore(scoreToAdd, mainScore):
    mainScore += int(scoreToAdd)


def decreaseScore(scoreToRemove, mainScore):
    mainScore -= int(scoreToRemove)


def runGTW():
    """
    This function provide list of alphabets to user and user shpuld guess 
    the word
    """
    clearTerminal()
    print("1 : Easy")
    print("2 : Medium")
    print("3 : Hard")
    level = input("Please select the level of the game\n")
    score = 0
    print("Guess the word with following letters.")
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
    if user_guess.lower() is word.lower():
        print("Good job, you found the word")
        increaseScore(level, score)
    else:
        print(f"{user_guess} is not the right answer, it's {word}")
        decreaseScore(level, score)


def main():
    """
    Main program functions
    """
    print("Lets select with game you wanna play")
    print("Enter 1 for  Rock, Paper, Scissors!")
    print("Enter 2 for guess the word!")
    game = input()
    clearTerminal()
    if game == '1':
        print(f"You selected Rock, Paper, Scissors. Good Luck!\n")
        runRPS()
    elif game == '2':
        print(f"You selected guess the word. Good Luck!\n")
        runGTW()


print("Welcome, Lets have some fan today!")
main()



