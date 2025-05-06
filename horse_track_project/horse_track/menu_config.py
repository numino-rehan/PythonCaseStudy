# coffee_machine/menu_config.py

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


DENOMINATIONS = [1,5,10,20,100]


HORSE_DATA = {
    1: {"name": "That Darn Gray Cat", "odds": 5,"won":True},
    2: {"name": "Fort Utopia", "odds": 10,"won":False},
    3: {"name": "Count Sheep", "odds": 9,"won":False},
    4: {"name": "Ms Traitour", "odds": 4,"won":False},
    5: {"name": "Real Princess", "odds": 3,"won":False},
    6: {"name": "Pa Kettle", "odds": 5,"won":False},
    7: {"name": "Gin Stinger", "odds": 7,"won":False}
}
