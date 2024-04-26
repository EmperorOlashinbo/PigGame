import unittest
import os
import json
from HighScores import HighScores


class TestHighScores(unittest.TestCase):
    def setUp(self):
        # Setup a temporary file to simulate high score storage
        self.filename = "test_highscores.json"
        with open(self.filename, "w") as file:
            file.write('{"Player1": 100, "Player2": 90}')

    def tearDown(self):
        # Clean up by removing the temporary file after each test
        os.remove(self.filename)

    def test_load_scores_existing_file(self):
        # Test loading scores from an existing file and verify the content is correct
        high_scores = HighScores(self.filename)
        self.assertEqual(high_scores.load_scores(), {"Player1": 100, "Player2": 90})

    def test_load_scores_nonexistent_file(self):
        # Test loading scores from a non-existing file should return an empty dictionary
        high_scores = HighScores("nonexistent_file.json")
        self.assertEqual(high_scores.load_scores(), {})

    def test_save_score_new_score(self):
        # Test saving a new score and verify it is added correctly
        high_scores = HighScores(self.filename)
        high_scores.save_score("Player3", 95)
        self.assertEqual(
            high_scores.scores, {"Player1": 100, "Player2": 90, "Player3": 95}
        )
        # Verify that the data was written to the file
        with open(self.filename, "r") as file:
            data = json.load(file)
            self.assertEqual(data, {"Player1": 100, "Player2": 90, "Player3": 95})

    def test_save_score_existing_score(self):
        # Test updating an existing score if the new score is higher
        high_scores = HighScores(self.filename)
        high_scores.save_score("Player1", 110)
        self.assertEqual(high_scores.scores, {"Player1": 110, "Player2": 90})
        # Verify that the data was updated in the file
        with open(self.filename, "r") as file:
            data = json.load(file)
            self.assertEqual(data, {"Player1": 110, "Player2": 90})


if __name__ == "__main__":
    unittest.main()
