# main.py

from coffee_machine.machine import CoffeeMachine

def main():
    c = CoffeeMachine()
    c.display_inventory()
    c.display_menu()
    
    while True:
        cmd = input("Enter a command:\n"
            "'R' or 'r' - restock the  inventory\n"
            "'Q' or 'q' - quit the application\n"
            "[1-6]  to order a coffee\n"
        )
        print("______________________________")
        c.process_commands(cmd)

if __name__ == "__main__":
    main()
