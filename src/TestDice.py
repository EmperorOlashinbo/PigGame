import unittest
from Player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Initialize a player with a name for each test
        self.player = Player("Test")

    def test_update_score_positive(self):
        # Test updating the player's score with a positive value
        self.player.update_score(5)
        self.assertEqual(self.player.score, 5, "Score should increase by 5")

    def test_update_score_negative(self):
        # Test updating the player's score with a negative value to simulate score penalties
        self.player.score = 10  # Initial score
        self.player.update_score(-3)
        self.assertEqual(
            self.player.score, 7, "Score should decrease by 3 due to penalty"
        )

    def test_update_score_multiple_times(self):
        # Test updating the score multiple times and verify final score
        updates = [5, 10, -2, 7]  # Sequence of score updates
        final_score = sum(updates)
        for update in updates:
            self.player.update_score(update)
        self.assertEqual(
            self.player.score, final_score, "Final score should reflect all updates"
        )

    def test_reset_score(self):
        # Ensure the player's score is reset to 0
        self.player.score = 10  # Set an initial score
        self.player.reset_score()
        self.assertEqual(self.player.score, 0, "Score should be 0 after reset")

    def test_reset_score_after_updates(self):
        # Test resetting the score after multiple updates
        updates = [15, -5, 10]  # Some score changes
        for update in updates:
            self.player.update_score(update)
        self.player.reset_score()
        self.assertEqual(
            self.player.score, 0, "Score should reset to 0 after multiple updates"
        )


if __name__ == "__main__":
    unittest.main()
