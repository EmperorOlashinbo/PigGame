import unittest
from DiceHand import DiceHand

class TestDiceHand(unittest.TestCase):
    def setUp(self):
        # Create a fresh instance of DiceHand for each test
        self.dice_hand = DiceHand()

    def test_add_and_total_roll(self):
        # Test that dice rolls are added correctly and total is computed accurately
        self.dice_hand.add_roll(4)
        self.dice_hand.add_roll(3)
        self.assertEqual(self.dice_hand.total(), 7, "Total should be the sum of all dice rolls")

    def test_multiple_adds_and_total_roll(self):
        # Test adding multiple rolls and verify the total
        rolls = [2, 5, 3, 6]  # Example dice rolls
        total_expected = sum(rolls)
        for roll in rolls:
            self.dice_hand.add_roll(roll)
        self.assertEqual(self.dice_hand.total(), total_expected, "Total should correctly sum multiple dice rolls")

    def test_reset(self):
        # Test that the dice hand can be reset to zero after adding some rolls
        self.dice_hand.add_roll(5)
        self.dice_hand.add_roll(2)  # Add more complexity to the test
        self.dice_hand.reset()
        self.assertEqual(self.dice_hand.total(), 0, "Total should be zero after reset")

    def test_total_after_reset_and_add(self):
        # Test the functionality of reset followed by new adds
        self.dice_hand.add_roll(3)
        self.dice_hand.reset()  # Reset the hand
        self.dice_hand.add_roll(6)  # Add new roll after reset
        self.assertEqual(self.dice_hand.total(), 6, "Total should be equal to the new roll after a reset")

if __name__ == "__main__":
    unittest.main()
