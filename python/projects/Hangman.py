import random
stages = [
'''
  -----
  |   |
      |
      |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
      |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
  |   |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|   |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|\\  |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|\\  |
 /    |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|\\  |
 / \\  |
      |
---------
'''
]
word = ["apple", "banana", "mango"]

computer_choice = random.choice(word)

user_word = ["-"] * len(computer_choice)

count = 1

while count <= 7:

    user_input = input("Enter a letter: ")

    if len(user_input) != 1:
        print("Invalid Input")

    else:
        if user_input in computer_choice:

            for i in range(len(computer_choice)):
                if computer_choice[i] == user_input:
                    user_word[i] = user_input

            print("".join(user_word))

        else:
            print(stages[count - 1])

        print(f"You used {count}/7 attempts")

    if "".join(user_word) == computer_choice:
        break

    count += 1

if "".join(user_word) == computer_choice:
    print(f"Congratulations! Word is {computer_choice}")
else:
    print(f"You lost! Word is {computer_choice}")