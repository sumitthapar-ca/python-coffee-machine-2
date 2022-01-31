from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem

coffe_make_obj = CoffeeMaker()
menu = Menu()

user_choice = input(f"What would you like? {menu.get_items()}: ")
print(user_choice)

if user_choice.lower() == menu.:
