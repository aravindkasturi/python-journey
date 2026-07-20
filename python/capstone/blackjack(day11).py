import random
import logocap1

print(logocap1.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():
    user = []
    computer = []

    # Deal initial cards
    for _ in range(2):
        user.append(random.choice(cards))
        computer.append(random.choice(cards))

    sum_user = sum(user)
    sum_computer = sum(computer)

    # Player's turn
    while True:
        print(f"\nYour cards: {user}, current score: {sum_user}")
        print(f"Computer's first card: {computer[0]}")

        if sum_user > 21:
            print("You went over. You lose.")
            return

        if sum_user == 21:
            print("Blackjack! You win!")
            return

        another = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if another == 'y':
            user.append(random.choice(cards))
            sum_user = sum(user)
        else:
            break

    # Computer's turn
    while sum_computer < 17:
        computer.append(random.choice(cards))
        sum_computer = sum(computer)

    print("\nYour final hand:", user, "Final score:", sum_user)
    print("Computer's final hand:", computer, "Final score:", sum_computer)

    # Decide winner
    if sum_computer > 21:
        print("Computer went over. You win!")
    elif sum_user > sum_computer:
        print("You won!")
    elif sum_user < sum_computer:
        print("You lost.")
    else:
        print("It's a draw.")


again = input("Do you want to start the game? 'y' or 'n': ").lower()

while again == "y":
    blackjack()
    again = input("\nDo you want to play again? 'y' or 'n': ").lower()

print("Thanks for playing!")