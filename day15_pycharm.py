# Day 15: Install Python and Coffee Machine Problem
# right-click on screen and split screen to dual wield files
# built-in linter: style conventions conforming to Pep8
# local history
# structure view shows outline of functions and variables in file
# right-click on function/var -> refactor -> rename. More intelligent than replace (major key)
# to-do tracking: put in program req.s as to-dos as # to-do (no hyphen)

# PROJECT: Coffee Machine Code
# inputs: type of drink requested
# outputs:
# global data: recipes, prices
# functions:
#   consume resources:
#       print report upon request,
#       check if resources sufficient
#   coin operated:
#       input Q to P
#       calculate return change or flag insufficient funds
import asciiArt
import math
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


# TODO: check for sufficient resources for selection
def resource_check(drink, stock):
    """checks for sufficient resources to make the user selection"""
    new_stock = stock
    insufficient = False
    for compound in new_stock:
        for drink_ing in MENU[drink]["ingredients"]:
            if compound == drink_ing:
                alpha = MENU[drink]["ingredients"][compound]
                new_stock[compound] -= alpha
                if new_stock[compound] < 0:
                    insufficient = True
    return [new_stock, insufficient]


# TODO: prompt user to input Q, D, N, P coins, calculate value
# TODO: check for sufficient funds or print change
def money_grab(price):
    """prompts for coins, returns change or insufficient funds message"""
    print(f"${price} is due")
    quarters = int(input("Please input your quarters: "))
    owed = price - quarters * 0.25
    print(f"${owed} is due")
    dimes = int(input("Please input your dimes: "))
    owed = owed - dimes * 0.10
    print(f"${owed} is due")
    nickels = int(input("Please input your nickels: "))
    owed = owed - nickels * 0.05
    print(f"${owed} is due")
    pennies = int(input("Please input your pennies: "))
    owed = owed - pennies * 0.01
    if owed < 0:
        print(f"You receive {owed*(-1)} back")
        return True
    elif owed == 0:
        print("Who carries enough coins for perfect change? Anyways, we're square.")
        return True
    else:
        return False


# TODO: prompt user to make a selection
def coffee_machine():
    """main function"""
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    cash_on_hand = 0
    print(asciiArt.homer)
    print("Welcome to Cafe de Homer")
    keep_vending = True
    while keep_vending:
        selection = input("Would you like an espresso, latte, or cappuccino? ").lower()
        if selection not in MENU:
            if selection == "report":
                for things in resources:
                    print(things)
                keep_vending = False
            elif selection == "off":
                keep_vending = False
            else:
                selection = input("Try again ")
        else:
            [new_resources, nope] = resource_check(selection, resources)
            if not nope:
                if money_grab(MENU[selection]["cost"]):
                    resources = new_resources
                    print(f"Here is your {selection}")
                    cash_on_hand += MENU[selection]["cost"]
                    print(resources)
                    print(cash_on_hand)
                    keep_vending = False

                else:
                    print("Sorry, you don't have enough funds for that")
                    keep_vending = input("Would you like to start over? [y/n]").lower() == "y"
                # TODO: off and report inputs - report shows input values

# coffee_machine()
# my_choice = "espresso"
# if my_choice in MENU:
#     print(MENU[my_choice]["cost"])
# else:
#     print("typo")
x = 5
y = x
y += 5
print(y)
