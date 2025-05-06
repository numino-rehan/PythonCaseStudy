import sys

INGREDIENT_PRICES = {
    "Coffee": 0.75,
    "Decaf Coffee": 0.75,
    "Sugar": 0.25,
    "Cream": 0.25,
    "Steamed Milk": 0.35,
    "Foamed Milk": 0.35,
    "Espresso": 1.10,
    "Cocoa": 0.90,
    "Whipped Cream": 1.00
}

DRINK_MENU = {
    "Coffee": {"Coffee": 3, "Sugar": 1, "Cream": 1},
    "Decaf Coffee": {"Decaf Coffee": 3, "Sugar": 1, "Cream": 1},
    "Caffe Latte": {"Espresso": 2, "Steamed Milk": 1},
    "Caffe Americano": {"Espresso": 3},
    "Caffe Mocha": {"Espresso": 1, "Cocoa": 1, "Steamed Milk": 1, "Whipped Cream": 1},
    "Cappuccino": {"Espresso": 2, "Steamed Milk": 1, "Foamed Milk": 1}
}

MAX_STOCK = 10


class CoffeeMachine:
    def __init__(self):
        self.inventory = {ingredient: MAX_STOCK for ingredient in sorted(INGREDIENT_PRICES)}
        self.id_to_drink = {}
        self.menu = self.generate_menu()

    def generate_menu(self):
        menu = {}
        count = 1
        sorted_drinks = sorted(DRINK_MENU.keys())
        self.id_to_drink = {}
        for drink in sorted_drinks:
            cost = 0
            in_stock = True
            for ingredient, qty in DRINK_MENU[drink].items():
                cost += INGREDIENT_PRICES[ingredient] * qty
                if self.inventory[ingredient] < qty:
                    in_stock = False
            menu[drink] = {
                "item_id": count,
                "cost": round(float(cost), 2),
                "in_stock": in_stock
            }
            self.id_to_drink[str(count)] = drink
            count += 1
        return menu

    def restock(self):
        self.inventory = {ingredient: MAX_STOCK for ingredient in self.inventory}
        self.menu = self.generate_menu()

    def can_make(self, drink):
        for ingredient, qty in DRINK_MENU[drink].items():
            if self.inventory[ingredient] < qty:
                return False
        return True

    def deduct_ingredients(self, drink):
        for ingredient, qty in DRINK_MENU[drink].items():
            self.inventory[ingredient] -= qty

    def print_menu(self):
        for drink, info in sorted(self.menu.items(), key=lambda x: x[1]["item_id"]):
            status = "In Stock" if info["in_stock"] else "Out of Stock"
            print(f'{info["item_id"]}. {drink}, ${info["cost"]:.2f}, {status}')

    def process_commands(self, command):
        command = command.strip()
        if not command:
            return
        if command == "q":
            print("Exiting. Goodbye!")
            sys.exit()
        elif command == "r":
            self.restock()
            print("Inventory restocked.")
            self.print_menu()
        elif command in self.id_to_drink:
            drink = self.id_to_drink[command]
            if self.menu[drink]["in_stock"]:
                self.deduct_ingredients(drink)
                print(f"Dispensing: {drink}")
                self.menu = self.generate_menu()
            else:
                print(f"Out of stock: {drink}")
            self.print_menu()
        else:
            print("Invalid selection.")
            self.print_menu()


# Main loop
c = CoffeeMachine()
c.print_menu()
while True:
    cmd = input("Enter command (1-6, r to restock, q to quit): ")
    c.process_commands(cmd)
