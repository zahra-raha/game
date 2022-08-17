import random


def runRPS(game):
    """
    this is the main function to play Rock, Paper,
    """
    choices = ["Rock", "Paper", "Scissors"]
    print(f"You selected {game}. Good Luck!\n")
    user_score = 0
    computer_score = 0
    contin = True

    while contin is True:
        while True:
            print(" 1 : Rock \n 2 : Paper\n 3 : Scissors")
            choice = input("Please choose 1, 2, 3 or enter e to exit:\n")
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
    print("Thanks for playing")           


def main():
    """
    Main program functions
    """
    USER_NAME = input("Please enter your name: \n")

    print(f"Hello {USER_NAME}. Welcome play zoon!")
    print("Lets select with game you wanna play today")
    print("Enter 1 for  Rock, Paper, Scissors!")
    game = input()

    if game == '1':
        runRPS(game)


print("Lets have some fan today!")
main()



