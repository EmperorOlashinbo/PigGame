class Intelligence:
    def __init__(self, level="medium"):
        # Initialize the AI with a difficulty level. Default level is "medium".
        self.level = level

    def should_roll_again(self, current_score, turn_score):
        # Determine whether the AI should roll again based on the game's current score, the turn score,
        # and the AI's difficulty level.

        if self.level == "easy":
            # For 'easy' level, AI rolls again if the turn score is less than 15.
            return turn_score < 15
        elif self.level == "medium":
            # For 'medium' level, AI rolls again if the turn score is less than 20,
            # or the combined current and turn scores are less than 100.
            return turn_score < 20 or current_score + turn_score < 100
        else:
            # For 'hard' and other levels, set a risk threshold based on the game's progress:
            # If the combined score is less than 70, risk threshold is 25, otherwise, it's 15.
            risk_threshold = 25 if current_score + turn_score < 70 else 15
            return turn_score < risk_threshold
