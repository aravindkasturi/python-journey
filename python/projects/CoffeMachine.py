from main import MENU, resources
import sys


def is_resources_sufficient(resources, MENU):
    if user_input == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
            if resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
                process_coins()
            else:
                print("Sorry there is not enough coffee")
        else:
            print("Sorry there is not enough water")

    elif user_input == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
            if resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
                if resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
                    process_coins()
                else:
                    print("Sorry there is not enough coffee")
            else:
                print("Sorry there is not enough milk")
        else:
            print("Sorry there is not enough water")

    elif user_input == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]:
            if resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
                if resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
                    process_coins()
                else:
                    print("Sorry there is not enough coffee")
            else:
                print("Sorry there is not enough milk")
        else:
            print("Sorry there is not enough water")


def process_coins():
    print("Please insert coins:")

    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nickles? "))
    pennies = float(input("How many pennies? "))

    total_coins = quarters + dimes + nickles + pennies

    if total_coins == MENU[user_input]["cost"]:
        print("Coins are sufficient")

    elif total_coins > MENU[user_input]["cost"]:
        x = MENU[user_input]["cost"]
        print(f"Coins inserted more. Money {total_coins-x} will be refunded")

    else:
        print("Coins are less. Money refunded")


# ---------------- Main Program ----------------

user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

if user_input == "report":
    for i, j in resources.items():
        print(f"{i}: {j}")

elif user_input == "off":
    sys.exit()

elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
    is_resources_sufficient(resources, MENU)

else:
    print("Invalid input")