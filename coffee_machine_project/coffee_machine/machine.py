# coffee_machine/machine.py
from .menu_config import DRINK_MENU, INGREDIENT_PRICES, MAX_STOCK
import sys

class CoffeeMachine:
    def __init__(self):
        self.inventory = {ingredient:MAX_STOCK for ingredient in sorted(INGREDIENT_PRICES)}
        self.menu = self.generate_menu()

    
    def generate_menu(self):
        self.id_to_drink = {str(i):drink for i,drink in enumerate(sorted(DRINK_MENU),1)}
        menu = {
            drink:{
               "item_id":i,
               "cost":sum(INGREDIENT_PRICES[ite]*qty for ite,qty in DRINK_MENU[drink].items()),
               "in_stock":all(self.inventory[ite]>=qty for ite,qty in DRINK_MENU[drink].items())

            }
            for i,drink in enumerate(sorted(DRINK_MENU),1)
        }
        return menu
    
    def restock(self):
        self.inventory = {ingredient: MAX_STOCK for ingredient in self.inventory}
        self.menu = self.generate_menu()
    
    def can_make(self,drink):
        for ingredients,qty in DRINK_MENU[drink].items():
             if self.inventory[ingredients] < qty:
                return False
        return True
    
    def deduct_ingredients(self,drink):
        for ingredients,qty in DRINK_MENU[drink].items():
             self.inventory[ingredients] -= qty



    def process_commands(self,command):
        command = command.strip().lower()
        if not command:
            return
        if command == "q":
            sys.exit()
        elif command == "r":
            self.restock()
        elif int(command) > 0 and int(command) <= len(DRINK_MENU):
            
            drink = self.id_to_drink[command]
            if self.can_make(drink):
                print(f"Dispensing: {drink}")
                self.deduct_ingredients(drink)
                self.menu = self.generate_menu()
            else:
                print(f"Out of Stock: {drink}")
        else:
            print("Invalid Option: Please choose option from below")
        self.display_inventory()
        self.display_menu()
    
    def display_inventory(self):
        print("______________________________")
        print("INVENTORY:")
        for item,qty in self.inventory.items():
            print(f"{item} {qty}")
        print("______________________________")

    
    def display_menu(self):
        print("______________________________")
        print("MENU:")
        for drink,val in self.menu.items():
            price = f"${val['cost']:.2f}"
            available = val["in_stock"]
            item_id = val["item_id"]
            print(f"{item_id},{drink},{price},{available}")
        print("______________________________")


