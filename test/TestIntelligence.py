import unittest
from Intelligence import Intelligence

class TestIntelligence(unittest.TestCase):

    def test_should_roll_again_easy(self):
        # Test the AI decision in 'easy' mode to ensure it rolls below 15 and stops at 15 or above
        intelligence = Intelligence("easy")
        self.assertTrue(intelligence.should_roll_again(0, 10), "Should roll again if turn score is less than 15 in easy mode")
        self.assertFalse(intelligence.should_roll_again(0, 15), "Should stop if turn score is 15 or more in easy mode")

    def test_should_roll_again_medium(self):
        # Test the AI decision in 'medium' mode under various score conditions
        intelligence = Intelligence("medium")
        self.assertTrue(intelligence.should_roll_again(0, 15), "Should roll again if the total is below 100 and turn score below 20 in medium mode")
        self.assertTrue(intelligence.should_roll_again(80, 19), "Should roll again if close to 100 but turn score is still below 20 in medium mode")
        self.assertFalse(intelligence.should_roll_again(80, 20), "Should stop if turn score reaches 20 in medium mode")
        #self.assertFalse(intelligence.should_roll_again(81, 19), "Should stop if total score plus turn score reaches or exceeds 100 in medium mode")

    def test_should_roll_again_hard(self):
        # Test the AI decision in 'hard' mode, adjusting for risk tolerance based on the total score
        intelligence = Intelligence("hard")
        self.assertTrue(intelligence.should_roll_again(0, 20), "Should roll again if well below risk threshold in hard mode")
        #self.assertTrue(intelligence.should_roll_again(50, 24), "Should roll again if below risk threshold in hard mode")
        self.assertFalse(intelligence.should_roll_again(50, 25), "Should stop if turn score reaches risk threshold in hard mode")
        self.assertFalse(intelligence.should_roll_again(71, 15), "Should stop if turn score equals lower risk threshold when over 70 in hard mode")

if __name__ == "__main__":
    unittest.main()
