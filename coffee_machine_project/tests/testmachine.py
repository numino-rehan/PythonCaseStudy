import unittest
from coffee_machine.machine import CoffeeMachine
from coffee_machine.menu_config import MAX_STOCK, INGREDIENT_PRICES

class TestCoffeeMachine(unittest.TestCase):
    def test_initial_inventory(self):
        machine = CoffeeMachine()
        for ingredient in INGREDIENT_PRICES:
            self.assertEqual(machine.inventory[ingredient], MAX_STOCK)
    def test_restock_resets_inventory(self):
        machine = CoffeeMachine()
        # Manually deduct some ingredients
        for ingredient in machine.inventory:
            machine.inventory[ingredient] = 0
        machine.restock()
        # Assert all ingredients are reset to MAX_STOCK
        for ingredient in machine.inventory:
            self.assertEqual(machine.inventory[ingredient], MAX_STOCK)

    def test_dispense_drink_success(self):
        machine = CoffeeMachine()
        drink = list(machine.menu.keys())[0]  # Select the first drink from the menu
        
        # Ensure the machine can make the drink before dispensing
        if machine.can_make(drink):
            # Capture the output to verify correct messages are printed
            with self.assertLogs() as log:
                machine.process_commands(str(machine.menu[drink]["item_id"]))
            
            # Check if the output contains the dispensing message
            self.assertIn(f"Dispensing: {drink}", log.output[0])


if __name__ == 'main':

    unittest.main()