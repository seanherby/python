# This will keep playing rock paper scissors with you forever
import random
choices = ["scissors", "rock", "paper"]

while (user_choice := input("Do you want - rock, paper, or scissors?\n")) != 'quit':
    print("you chose " + str(user_choice))
    computer_choice = random.choice (choices)
    
    if not user_choice in choices:
        print("Invalid choice:", user_choice)
    elif computer_choice == user_choice:
        print("You tied")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        print("The computer choose " + computer_choice + ", So You win!")
    else:
        print("The computer choose " + computer_choice + ", So You lose, Computer Wins, MUAHAHAHAHA!")
