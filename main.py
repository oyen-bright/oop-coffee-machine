from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on=True

my_money_machine = MoneyMachine()
my_money_machine.report()
menu=Menu()

coffee_maker=CoffeeMaker()
coffee_maker.report()

while is_on:
    options=menu.get_items()
    user_choice=input(f"What would you like {options}")
    if user_choice=="off":
        is_on= False
    elif user_choice=="report":
        my_money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


