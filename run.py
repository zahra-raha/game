import random
def runRPS(game):
    """
    this is the main function to play Rock, Paper,
    """
    choices = ["Rock", "Paper", "Scissors"]
    print(f"You selected {game}. Good Luck!")
    
    while True:
        print(" 1 : Rock \n 2 : Paper\n 3 : Scissors")
        choice = input("Please choose 1, 2 or 3\n")
        if choice == '1':
            player_choice = 'Rock'
            break
        elif choice == '2':
            player_choice = 'Paper'
            break
        elif choice == '3':
            player_choice = 'Scissors'
            break
        else:
            print("You entered envalid value\n")

    computer_choice = random.choice(choices)
    print(f"your choice is:        {player_choice} \ncomputer choice is: {computer_choice}")

    if player_choice == computer_choice:
        print("it's a tie game!")
    elif player_choice == "Rock":
        if computer_choice == "Paper":
            print("you lost!")
        if computer_choice == "Scissors":
            print("you won!")
    elif player_choice == "Scissors":
        if computer_choice == "Rock":
            print("you lost!")
        if computer_choice == "Paper":
            print("you won!")
    elif player_choice == "Paper":
        if computer_choice == "Rock":
            print("you won!")
        if computer_choice == "Scissors":
            print("you lost!")
    elif player_choice == "finish":
        print("thanks for playing this game, have a great day!")
        

def main():
    """
    Main program functions
    """
    PLAYER_NAME = input("Please enter your name: \n")

    print(f"Hello {PLAYER_NAME}. Welcome play zoon!")
    print("Lets select with game you wanna play today")
    print("Enter 1 for  Rock, Paper, Scissors!")
    game = input()

    if game == '1':
        runRPS(game)


print("Lets have some fan today!")
main()



