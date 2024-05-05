class Player:
    def __init__(self, name):
        # Initialize the Player object with a name and an initial score of 0.
        self.name = name
        self.score = 0

    def update_score(self, points):
        # Update the player's score by adding a specified number of points.
        # This method can handle both positive and negative points for flexibility.
        self.score += points

    def reset_score(self):
        # Reset the player's score to 0, typically used at the start of a new game.
        self.score = 0
