from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Object creation
report=MoneyMachine()
report_ing=CoffeeMaker()
menu=Menu()
money_machine=MoneyMachine()


#main progroam

is_on=True

while is_on:
    options=menu.get_items()
    choice=input(f"What would you like? ({options}): ").lower()
    if choice=="off":
        is_on=False
    elif choice=="report":
        report.report()
        report_ing.report()
    else:
        drink=menu.find_drink(choice)
        if report_ing.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            (report_ing.make_coffee(drink))