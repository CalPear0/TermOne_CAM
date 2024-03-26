import random

options = ['rock', 'paper', 'scissors', 'lizard', 'spock']
player = None
computer = random.choice(options)

print()
rules = input("Would you like to see the rules for Rock Paper Scissors? (Type 'Yes' or 'No') ")
if rules == 'Yes':
    print("Scissors Cuts Papery\nPaper Covers Rock\nRock Crushes Lizard\nLizard Poisons Spock\nSpock Smashes Scissors\nScissors Decapitates Lizard\nLizard Eats Paper\nPaper Disproves Spock\nSpock Vaporizes Rock\nRock Smashes Scissors \n \n \n")

else:
    print("Sure, whatever. You may begin playing. \n \n")


    player = input("Choose an Option: Rock, Paper, Scissors, Lizard, or Spock: \n \n")

    print()
    print(f"Player: {player}")
    print(f"Computer: {computer}")

player = input("Choose an Option: Rock, Paper, Scissors, Lizard, or Spock: \n \n")

if player == computer:
    print("Draw!")

elif player == "Rock" and computer == "Scissors":
    print("You win! Rock Crushes Scissors! ")

elif player == "Scissors" and computer == "Paper":
    print("You win! Scissors Cuts Paper! ")

elif player == "Paper" and computer == "Rock":
    print("You win! Paper Covers Rock! ")

elif player == "Rock" and computer == "Lizard":
    print("You win! Rock Crushes Lizard! ")

elif player == "Lizard" and computer == "Spock":
    print("You win! Lizard Poisons Spock! ")

elif player == "Spock" and computer == "Scissors":
    print("You win! Spock Smashes Scissors! ")

elif player == "Scissors" and computer == "Lizard":
    print("You win! Scissors Decapitates Lizard! ")

elif player == "Lizard" and computer == "Paper":
    print("You win! Lizard Eats Paper! ")

elif player == "Paper" and computer == "Spock":
    print("You win! Paper Disproves Spock! ")

elif player == "Spock" and computer == "Rock":
    print("You win! Spock Vaporizes Rock! ")

elif computer == "Rock" and player == "Scissors":
    print("You lose! Rock Crushes Scissors! ")

elif computer == "Scissors" and player == "Paper":
    print("You lose! Scissors Cuts Paper! ")

elif computer == "Paper" and player == "Rock":
    print("You lose! Paper Covers Rock! ")

elif computer == "Rock" and player == "Lizard":
    print("You lose! Rock Crushes Lizard! ")

elif computer == "Lizard" and player == "Spock":
    print("You lose! Lizard Poisons Spock! ")

elif computer == "Spock" and player == "Scissors":
    print("You lose! Spock Smashes Scissors! ")

elif computer == "Scissors" and player == "Lizard":
    print("You lose! Scissors Decapitates Lizard! ")

elif computer == "Lizard" and player == "Paper":
    print("You lose! Lizard Eats Paper! ")

elif computer == "Paper" and player == "Spock":
    print("You lose! Paper Disproves Spock! ")

elif computer == "Spock" and player == "Rock":
    print("You lose! Spock Vaporizes Rock! ")

print()
print("Press any key to exit, otherwise press enter to continue. ")