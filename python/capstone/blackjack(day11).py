import logocap1
import random
print(logocap1.logo)
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
def blackjack():
    # start=input("Do you want to start the game 'y' for yes , 'n' for no: ").lower()
    user=[]
    sum_user=0
    sum_computer=0
    computer=[]
    while (sum_computer and sum_user)<17:
        count=0
        while count<2:
            card= random.choice(cards)
            user.append(card)
            com_card=random.choice(cards)
            computer.append(com_card)
            count+=1
        sum_user=sum(user)
        sum_computer=sum(computer)
        print(f"Your cards: {user}, current score: {sum_user}")
        print(f"Computer's first card: {computer[0]}")
        another=input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another=='y':
                card= random.choice(cards)
                user.append(card)
                if sum_computer<17:
                    com_card=random.choice(cards)
                    computer.append(com_card)
                sum_user=sum(user)
                sum_computer=sum(computer)
                print(f"Your cards: {user}, current score: {sum_user}")
                print(f"Computer's first card: {computer[0]}")
        elif another=='n':
                if sum_computer<17:
                    com_card=random.choice(cards)
                    computer.append(com_card)
                    print(f"Your cards: {user}, current score: {sum(user)}")
                    print(f"Computer's first card: {computer[0]}")
    final_user=abs(21-sum_user)
    final_computer=abs(21-sum_computer)
    winner=min(final_user,final_computer)
    print(f"Your final hand: {user}, final score: {sum(user)}")
    print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
    if winner==final_user:
        print("You won, Congrats!")
    else:
        print("You lost")
again = input("Do you want to start the game 'y' for yes , 'n' for no: ").lower()

while again == 'y':
    blackjack()
    again = input("Do you want to play again? 'y' or 'n': ").lower()