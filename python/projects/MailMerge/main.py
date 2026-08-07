PLACEHOLDER="[name]"



with open("./Input/Names/invited_names.txt") as names_file:
    names=names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    s=letter.read()

    for name in names:
        new_letter=s.replace(PLACEHOLDER,name.strip())
        with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as letter:
            letter.write(new_letter)
