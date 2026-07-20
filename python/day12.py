#local scope and global scope

#scope--visibilty

# enemies=1   #global scope

# def increase_enemies():
#     enemies=2   #local scope
#     print(f"enemies inside fun: {enemies}")

# increase_enemies()
# print(f"enemies outside fun: {enemies}")

#block scope it is supported in python and not supported in java/c++

"""in python even we define a variable inside a block such a if etc it can be accessed anywhere in
program"""

# game_level=3
# enemies=["virat","dhoni","rohit"]


# if game_level<5:
#     new_enemy=enemies[0]  #vairable defined inside a if block
# print(new_enemy)  # can be accessed outside block also

# prime
def is_prime(num):
    if num==1:
        return False
    if num==2:
        return True
    for i in range(2,num):
        if num%i==0:
            return False
    return True
out=is_prime(int(input()))
print(out)