import json
import os


class HighScores:
    def __init__(self, filename="highscores11.json"):
        # Initialize the HighScores object with a file name for storing high scores.
        # The default filename is "highscores11.json".
        self.filename = filename
        self.scores = self.load_scores()

    def load_scores(self):
        # Load scores from a JSON file if it exists, otherwise, return an empty dictionary.
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return {}

    def save_score(self, name, score):
        # Save a player's highest score to the JSON file.
        # If the player already has a recorded score, it updates only if the new score is higher.
        self.scores[name] = max(score, self.scores.get(name, 0))
        with open(self.filename, "w") as file:
            json.dump(self.scores, file)

    def display(self):
        # Display all high scores sorted from highest to lowest.
        for name, score in sorted(
            self.scores.items(), key=lambda item: item[1], reverse=True
        ):
            print(f"{name}: {score}")
