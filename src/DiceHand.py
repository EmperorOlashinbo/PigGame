class DiceHand:
    def __init__(self):
        # Initialize the DiceHand object with an empty list to store dice rolls.
        self.rolls = []

    def add_roll(self, roll):
        # Add a single dice roll to the list of rolls.
        self.rolls.append(roll)

    def total(self):
        # Calculate and return the total sum of all dice rolls in the list.
        return sum(self.rolls)

    def reset(self):
        # Reset the list of dice rolls to an empty list, clearing all the previous rolls.
        self.rolls = []
