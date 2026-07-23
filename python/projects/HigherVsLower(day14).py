import random
from dataday14 import data
from art import logo, vs

print(logo)

score = 0
a = random.choice(data)


def hvl(score, a):
    # Choose a different B
    b = random.choice(data)
    while a == b:
        b = random.choice(data)

    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")

    # Keep asking until input is valid
    while True:
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if guess in ("A", "B"):
            break
        print("Invalid input. Please enter A or B.")

    if guess == "A":
        if a["follower_count"] > b["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}")
            hvl(score, a)
        else:
            print(f"You lost. Final score: {score}")

    else:  # guess == "B"
        if b["follower_count"] > a["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}")
            hvl(score, b)
        else:
            print(f"You lost. Final score: {score}")


hvl(score, a)