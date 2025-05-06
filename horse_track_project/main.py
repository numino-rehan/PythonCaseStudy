# main.py

from horse_track.machine import ATMMachine

def main():
    a = ATMMachine()
    a.show_inventory()
    a.show_horse_data()
    while True:
        command = input(
            "Enter a command:\n"
            "'R' or 'r' - restock the cash inventory\n"
            "'Q' or 'q' - quit the application\n"
            "'W' or 'w' [1-7] - set the winning horse number\n"
            "[1-7] <amount> - place a bet of the given amount on a specific horse\n"
        )
        print("______________________________")
        a.process_commands(command)
        a.show_inventory()
        a.show_horse_data()

if __name__ == "__main__":
    main()