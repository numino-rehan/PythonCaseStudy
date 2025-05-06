# main.py

from coffee_machine.machine import CoffeeMachine

def main():
    c = CoffeeMachine()
    c.display_inventory()
    c.display_menu()
    
    while True:
        cmd = input("Enter command (1-6, r to restock, q to quit): ")
        print("______________________________")
        c.process_commands(cmd)

if __name__ == "__main__":
    main()
