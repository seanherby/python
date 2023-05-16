import random

# This generates a random dice roll for 2 die
def roll_dice():
    dice_total = roll1 = random.randint(1,6) + random.randint(1,6)
    return dice_total

# You and a friend both roll dice and the program tells you who wins
def main():
    player1 = input("Enter Player 1 name: ")
    if player1 == '':
        player1 = "Payer 1"
    player2 = input("Enter Player 2 name: ")
    if player2 == '':
        player2 = "Payer 2"

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, "rolled a", roll1)
    print(player2, "rolled a", roll2)

    if roll1 > roll2:
        print(player1, "won")
    elif roll1 < roll2:
        print(player2, "won")
    else:
        print("they tied")

main()
