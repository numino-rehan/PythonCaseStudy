# coffee_machine/machine.py
from .menu_config import DENOMINATIONS, MAX_STOCK, HORSE_DATA
import sys
from colorama import Fore, Style, init

init(autoreset=True)

class ATMMachine:
    def __init__(self):
        self.inventory = {denominations: MAX_STOCK for denominations in sorted(DENOMINATIONS)}
        self.horse_data = self.generate_horse_data()

    def generate_horse_data(self):
        return HORSE_DATA

    def restock(self):
        self.inventory = {denominations: MAX_STOCK for denominations in sorted(DENOMINATIONS)}
        print(Fore.GREEN + "Restocking Complete")
        print()

    def set_winner(self, horse_id, won=True):
        self.horse_data[horse_id]["won"] = won
        print(Fore.GREEN + f'Set "{self.horse_data[horse_id]["name"]}" (Horse #{horse_id}) as the winning horse.')
        print()

    def show_inventory(self):
        print(Fore.BLUE + Style.BRIGHT + "INVENTORY:")
        for den, qty in self.inventory.items():
            print(Fore.YELLOW + f"${den:.2f}" + Fore.WHITE + f" x {qty}")
        print()

    def show_horse_data(self):
        print(Fore.BLUE + Style.BRIGHT + "HORSES:")
        for horse_id, data in self.horse_data.items():
            name = data["name"]
            odds = data.get("odds", "N/A")
            won = data.get("won", False)

            status_color = Fore.GREEN if won else Fore.RED
            status_text = "WON" if won else "LOST"

            print(f"{Fore.YELLOW}{horse_id}{Style.RESET_ALL}, "
                  f"{Fore.CYAN}{name}{Style.RESET_ALL}, "
                  f"{Fore.WHITE}{odds}{Style.RESET_ALL}, "
                  f"{status_color}{status_text}")
        print()

    def dispense_cash(self, amount):
        remaining = amount
        dispensed = {}

        for denomination in sorted(self.inventory.keys(), reverse=True):
            while remaining >= denomination and self.inventory[denomination] > 0:
                dispensed[denomination] = dispensed.get(denomination, 0) + 1
                self.inventory[denomination] -= 1
                remaining = round(remaining - denomination, 2)

        if remaining > 0:
            print(Fore.RED + Style.BRIGHT + "Insufficient funds in machine.")
            print()
            # Restore inventory
            for denom, count in dispensed.items():
                self.inventory[denom] += count
            return

        print(Fore.GREEN + "Dispensing Cash:")
        for denom, count in sorted(dispensed.items()):
            print(Fore.YELLOW + f"${denom:.2f}:" + Fore.WHITE + f" {count}")
        print()

    def process_commands(self, command):
        command = command.strip().lower()
        if not command:
            return

        cmd = command.split()

        if command == "q":
            sys.exit()

        elif command == "r":
            self.restock()

        elif command.startswith("w"):
            if len(cmd) != 2:
                print(Fore.RED + f"Invalid Command: {command}")
                print()
            else:
                horse_id = cmd[1]
                if horse_id.isdigit():
                    horse_id = int(horse_id)
                    if 1 <= horse_id <= len(HORSE_DATA):
                        self.set_winner(horse_id)
                    else:
                        print(Fore.RED + f"Invalid Horse Number: {horse_id}")
                        print()
                else:
                    print(Fore.RED + f"Invalid Horse Number: {cmd[1]}")
                    print()

        elif command[0].isdigit():
            if len(cmd) != 2:
                print(Fore.RED + f"Invalid Command: {command}")
                print()
            else:
                horse_id, amount = cmd[0], cmd[1]
                if horse_id.isdigit():
                    horse_id = int(horse_id)
                    if 1 <= horse_id <= len(HORSE_DATA):
                        if amount.isdigit():
                            amount = int(amount)
                            if amount <= 0:
                                print(Fore.RED + f"Invalid Bet: {amount}")
                                print()
                            elif self.horse_data[horse_id]["won"]:
                                winnings = amount * self.horse_data[horse_id]["odds"]
                                print(Fore.GREEN + f"Payout: {self.horse_data[horse_id]['name']}, ${winnings}")
                                print()
                                self.dispense_cash(winnings)
                            else:
                                print(Fore.YELLOW + f"No Payout: {self.horse_data[horse_id]['name']}")
                                print()
                        else:
                            print(Fore.RED + f"Invalid Bet: {amount}")
                            print()
                    else:
                        print(Fore.RED + f"Invalid Horse Number: {horse_id}")
                        print()
                else:
                    print(Fore.RED + f"Invalid Horse Number: {horse_id}")
                    print()

        else:
            print(Fore.RED + f"Invalid Command: {command}")
            print()
