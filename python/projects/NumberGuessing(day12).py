import random
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 10.")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
actual_num=random.randint(1,10)
if difficulty=="hard":
    def hard_level():
        count=3
        while count>0:
            print(f"You have {count} attempts remaining to guess the number.")
            num=int(input("Make a guess: "))
            if num==actual_num:
                print(f"Congratulations! You guessed the number that is {actual_num}")
                break
            elif num>actual_num:
                print("Too high\nGuess again")
            else:
                print("Too low\n Guess again")
            count-=1
        if count==0:
            print("You've run out of guesses, you lose.")
    hard_level()
elif difficulty=="easy":
    def easy_level():
        count=5
        while count>0:
            print(f"You have {count} attempts remaining to guess the number.")
            num=int(input("Make a guess: "))
            if num==actual_num:
                print (f"Congratulations! You guessed the number that is {actual_num}")
                break
            elif num>actual_num:
                print("Too high\nGuess again")
            else:
                print("Too low\n Guess again")
            count-=1
        if count==0:
            print("You've run out of guesses, you lose.")
    easy_level()
else:
    print("Invalid Input")
