import random
play_again = "y"

while play_again == "y":

    print()
    rules = input("Would you like to see the rules for Rock Paper Scissors? (y/n) ")
    if rules == 'y':
        print("Scissors Cuts Papery\nPaper Covers Rock\nRock Crushes Lizard\nLizard Poisons Spock\nSpock Smashes Scissors\nScissors Decapitates Lizard\nLizard Eats Paper\nPaper Disproves Spock\nSpock Vaporizes Rock\nRock Smashes Scissors \n \n \n")

    else:
        print("Sure, whatever. You may begin playing. \n \n")

    player = input("Choose an Option: Rock, Paper, Scissors, Lizard, or Spock: \n \n")

    options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    computer = random.choice(options)

    print()
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Draw! (Computer Chose Same Option) ")
    elif player == "Rock" and computer == "Scissors":
        print("You win! Rock Crushes Scissors (Computers Choice)! ")
    elif player == "Scissors" and computer == "Paper":
        print("You win! Scissors Cuts Paper (Computers Choice)! ")
    elif player == "Paper" and computer == "Rock":
        print("You win! Paper Covers Rock (Computers Choice)! ")
    elif player == "Rock" and computer == "Lizard":
        print("You win! Rock Crushes Lizard (Computers Choice)! ")
    elif player == "Lizard" and computer == "Spock":
        print("You win! Lizard Poisons Spock (Computers Choice)! ")
    elif player == "Spock" and computer == "Scissors":
        print("You win! Spock Smashes Scissors (Computers Choice)! ")
    elif player == "Scissors" and computer == "Lizard":
        print("You win! Scissors Decapitates Lizard (Computers Choice)! ")
    elif player == "Lizard" and computer == "Paper":
        print("You win! Lizard Eats Paper (Computers Choice)! ")
    elif player == "Paper" and computer == "Spock":
        print("You win! Paper Disproves Spock (Computers Choice)! ")
    elif player == "Spock" and computer == "Rock":
        print("You win! Spock Vaporizes Rock (Computers Choice)! ")
    elif player == "Scissors" and computer == "Rock":
        print("You lose! Rock (Computers Choice) Crushes Scissors! ")
    elif player == "Paper" and computer == "Scissors":
        print("You lose! Scissors (Computers Choice) Cuts Paper! ")
    elif player == "Rock" and computer == "Paper":
        print("You lose! Paper (Computers Choice) Covers Rock! ")
    elif player == "Lizard" and computer == "Rock":
        print("You lose! Rock (Computers Choice) Crushes Lizard! ")
    elif player == "Spock" and computer == "Lizard":
        print("You lose! Lizard (Computers Choice) Poisons Spock! ")
    elif player == "Scissors" and computer == "Spock":
        print("You lose! Spock (Computers Choice) Smashes Scissors! ")
    elif player == "Lizard" and computer == "Scissors":
        print("You lose! Scissors (Computers Choice) Decapitates Lizard! ")
    elif player == "Paper" and computer == "Lizard":
        print("You lose! Lizard (Computers Choice) Eats Paper! ")
    elif player == "Spock" and computer == "Paper":
        print("You lose! Paper (Computers Choice) Disproves Spock! ")
    elif player == "Rock" and computer == "Spock":
        print("You lose! Spock (Computers Choice) Vaporizes Rock! ")

    play_again = input("Would you like to continue playing? (y/n) ")
    if play_again == 'y':
        print()
    if play_again == 'n':
        print("Thanks for Playing Lil Bro! ")
