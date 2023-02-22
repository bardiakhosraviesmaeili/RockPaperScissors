import random

choices = ["ROCK", "PAPER", "SCISSORS"]

name = input("Hello\nPlease enter your name:")
print("Options : [ Rock , Paper , Scissors]")
player_choice = None

newgame = True

while newgame:
    computer_choice = random.choice(choices)
    while player_choice not in choices:
        player_choice = input("Please enter one of the option that you choise:").upper()
    print("You choose " + player_choice)
    print("The computer choice is " + computer_choice)
    if (computer_choice == "ROCK"):
        if (player_choice == "SCISSORS"):
            print("____Computer wins____")
    if (computer_choice == "SCISSORS"):
        if (player_choice == "PAPER"):
            print("____Computer wins____")
    if (computer_choice == "PAPER"):
        if (player_choice == "ROCK"):
            print("____Computer wins____")
    if (player_choice == "PAPER"):
        if (computer_choice == "ROCK"):
            print("____" + name + " wins____")
    if (player_choice == "SCISSORS"):
        if (computer_choice == "PAPER"):
            print("____" + name + " wins____")
    if (player_choice == "ROCK"):
        if (computer_choice == "SCISSORS"):
            print("____" + name + " wins____")
    if (player_choice == computer_choice):
        print("____Tie____")

    newgame = input("Do you want to play again?(Y/N)")
    if newgame.upper() == "N":
        print("HAVE A NICE DAY!")
        newgame = False
    player_choice = None
