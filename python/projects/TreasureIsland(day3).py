print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; |___|___________________
*******************************************************************************
                            TREASURE CHEST
                               💰💰💰
''')

print("Welcome to Treasure Island.\nYour Mission is to find the treasure")
print("You're at a cross road.")
cross_road=input("Where do you want to go?\n Type 'left' or 'right' ")
if cross_road=='right':
    print("Game Over")
elif cross_road=='left':
    print("You've come to a lake. There is an island in the middle of the lake.")
    next=input("Type 'wait' to wait for a boat. Type 'swim' to swim across ")
    if next=='swim':
        print("Game Over")
    elif next=='wait':
        print("You arrive at the island unharmed.\nThere are 3 doors. One red, one yellow and one blue.")
        color=input("Which color do you choose?")
        if color=='yellow':
            print("You won! Congratulations...")
        else:
            print("Game Over")
    else:
        print("invalid input")
else:
    print("invalid input")
