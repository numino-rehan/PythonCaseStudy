# coffee_machine/machine.py
from .menu_config import DENOMINATIONS,MAX_STOCK,HORSE_DATA
import sys

class ATMMachine:
    def __init__(self):
        self.inventory = {denominations:MAX_STOCK for denominations in sorted(DENOMINATIONS)}
        self.horse_data = self.generate_horse_data()


    def generate_horse_data(self):
        return HORSE_DATA
    
    def restock(self):
        self.inventory = {denominations:MAX_STOCK for denominations in sorted(DENOMINATIONS)}
        print("Restocking Complete")
    
    def set_winner(self,horse_id,won=True):
        print("______________________________")
        self.horse_data[horse_id]["won"] = won
        print(f'\033[92mSet "{self.horse_data[horse_id]["name"]}" (Horse #{horse_id}) as the winning horse.\033[0m')
        print("______________________________")

    
    def show_inventory(self):
        print("______________________________")
        print("INVENTORY:")
        for den,qty in self.inventory.items():
            print(f"${den:.2f} {qty}")
        print("______________________________")
    
    def show_horse_data(self):
        print("______________________________")
        print("HORSES:")
        for horse_id, data in self.horse_data.items():
            name = data["name"]
            odds = data.get("odds", "N/A")
            status = "won" if data.get("won") else "lost"
            print(f"{horse_id},{name},{odds},{status}")
        print("______________________________")


    def dispense_cash(self, amount):
        remaining = amount
        dispensed = {}
        
        for denomination in sorted(self.inventory.keys(), reverse=True):
            while remaining >= denomination and self.inventory[denomination] > 0:
                if denomination not in dispensed:
                    dispensed[denomination] = 0
                dispensed[denomination] += 1
                self.inventory[denomination] -= 1
                remaining = round(remaining - denomination, 2)
        
        if remaining > 0:
            print("\033[91mInsufficient funds in machine\033[0m")
            # Restore inventory
            for denom, count in dispensed.items():
                self.inventory[denom] += count
            return
        
        for denom, count in sorted(dispensed.items()):
            print(f"${denom:.2f}: {count}")



    def process_commands(self,command):
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
                print(f"Invalid Command: {command}")
            else:
                horse_id = cmd[1]
                if horse_id.isdigit():
                    horse_id = int(horse_id)
                    if 1 <= horse_id <= len(HORSE_DATA):
                        self.set_winner(horse_id)
                    else:
                        print(f"Invalid Horse Number: {horse_id}")
                else:
                    print(f"Invalid Horse Number: {cmd[1]}")

        elif command[0].isdigit():
            cmd = command.split()
            if len(cmd) != 2:
                print(f"\033[91mInvalid Command: {command}\033[0m")
            else:
                horse_id, amount = cmd[0], cmd[1]
                if horse_id.isdigit():
                    horse_id = int(horse_id)
                    if 1 <= horse_id <= len(HORSE_DATA):
                        if amount.isdigit():
                            amount = int(amount)
                            if amount <= 0:
                                print(f"\033[91mInvalid Bet: {amount}\033[0m")
                            elif self.horse_data[horse_id]["won"]:
                                winnings = amount * self.horse_data[horse_id]["odds"]
                                print(f"\033[92mPayout: {self.horse_data[horse_id]['name']}, ${winnings}\033[0m")
                                print("Dispensing:")
                                self.dispense_cash(winnings)
                            else:
                                print(f"\033[93mNo Payout: {self.horse_data[horse_id]['name']}\033[0m")
                        else:
                            print(f"\033[91mInvalid Bet: {amount}\033[0m")
                    else:
                        print(f"\033[91mInvalid Horse Number: {horse_id}\033[0m")
                else:
                    print(f"\033[91mInvalid Horse Number: {horse_id}\033[0m")

        else:
            print(f"Invalid Command {command}")


