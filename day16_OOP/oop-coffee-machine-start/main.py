from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import asciiArt
menu_items = MenuItem
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def coffee_machine():
    print(asciiArt.homer)
    print("Welcome to Cafe de Homer")
    keep_vending = True
    while keep_vending:
        selection = input(f"Choose from one of these items: {menu.get_items()}\n").lower()
        drink_deets = menu.find_drink(selection)
        if drink_deets is not None:
            if coffee_maker.is_resource_sufficient(drink_deets):
                coffee_maker.report()
                print(f"A {drink_deets.name} costs ${drink_deets.cost}")
                if money_machine.make_payment(drink_deets.cost):
                    money_machine.report()
                    coffee_maker.make_coffee(drink_deets)
                    coffee_maker.report()
        keep_vending = input("Are you done? [y/n] ").lower() == "n"

coffee_machine()
