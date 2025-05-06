import unittest
from horse_track.machine import ATMMachine
from horse_track.menu_config import DENOMINATIONS, MAX_STOCK

class TestATMMachine(unittest.TestCase):
    def test_restock_fills_inventory(self):
        atm = ATMMachine()
        atm.inventory = {denom: 0 for denom in DENOMINATIONS}  # Simulate empty inventory
        atm.restock()

        for denom in DENOMINATIONS:
            self.assertEqual(atm.inventory[denom], MAX_STOCK, f"Denomination ${denom} not restocked correctly.")

    def test_set_winner_marks_horse_as_won(self):
        atm = ATMMachine()
        horse_id = list(atm.horse_data)[1]
        atm.horse_data[horse_id]["won"]= False
        atm.set_winner(horse_id)
        self.assertTrue(atm.horse_data[horse_id]["won"], f"Horse #{horse_id} should be marked as winner.")

    def test_first_horse_as_won(self):
        atm = ATMMachine()
        horse_id = next(iter(atm.horse_data))
        won = atm.horse_data[horse_id]["won"]
        self.assertTrue(won,f"Horse #{horse_id} should be marked as winner.")
    
    def test_dispense_cash_reduces_inventory(self):
        atm = ATMMachine()
        # Set predictable inventory (3x $5, 3x $1)
        atm.inventory = {1: 3, 5: 3, 10: 0, 20: 0, 50: 0, 100: 0}

        # Try to dispense $11 (should use 2 x $5 and 1 x $1)
        atm.dispense_cash(11)

        self.assertEqual(atm.inventory[5], 1, "Expected 2 x $5 to be dispensed")
        self.assertEqual(atm.inventory[1], 2, "Expected 1 x $1 to be dispensed")

    def test_dispense_cash_restores_inventory_on_failure(self):
        atm = ATMMachine()
        # Set limited inventory: only $5 bills, not enough to pay $20
        atm.inventory = {1: 0, 5: 2, 10: 0, 20: 0, 50: 0, 100: 0}
        original_inventory = atm.inventory.copy()

        atm.dispense_cash(20)  # Can't dispense $20 with only 2x $5 bills

        # Ensure inventory is restored exactly
        self.assertEqual(atm.inventory, original_inventory, "Inventory should be restored if dispense fails.")
    
    def test_no_payout_for_losing_horse(self):
        atm = ATMMachine()
        horse_id = next(iter(atm.horse_data))
        atm.horse_data[horse_id]["won"] = False

        initial_inventory = atm.inventory.copy()
        bet_amount = 3

        atm.process_commands(f"{horse_id} {bet_amount}")

        # Inventory should be unchanged
        self.assertEqual(atm.inventory, initial_inventory)





if __name__ == 'main':

    unittest.main()