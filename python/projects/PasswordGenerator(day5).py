import random
letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

numbers = [
    '0','1','2','3','4','5','6','7','8','9'
]

symbols = [
    '!','@','#','$','%','^','&','*','(',')',
    '_','+','-','=','[',']','{','}','|','\\',
    ';',':',"'",'"',',','.','<','>','/','?',
    '`','~'
]

print("Welcome to the password generator!")
nr_letters=int(input("How many letters would you like to use in you password? "))
nr_symbols=int(input("How many symbils would you like to use? "))
nr_num=int(input("how many numbers would you like to use? "))
password=""
for char in range(1,nr_letters+1):
    random_choice = random.choice(letters)
    password+=random_choice
for char in range(1,nr_symbols+1):
    random_choice = random.choice(symbols)
    password+=random_choice
for char in range(1,nr_num+1):
    random_choice = random.choice(numbers)
    password+=random_choice
print(f"Generated password is {password}")
