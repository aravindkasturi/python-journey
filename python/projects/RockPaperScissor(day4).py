import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissor]

inp = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissor: "))

if inp < 0 or inp > 2:
    print("Invalid choice!")
else:
    computer_choice = random.randint(0, 2)

    print("You chose:")
    print(choices[inp])

    print("Computer chose:")
    print(choices[computer_choice])

    if inp == computer_choice:
        print("Draw")
    elif (
        (inp == 0 and computer_choice == 2) or
        (inp == 1 and computer_choice == 0) or
        (inp == 2 and computer_choice == 1)
    ):
        print("You Won!")
    else:
        print("You Lose!")