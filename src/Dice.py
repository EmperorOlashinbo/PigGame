import random


class Dice:
    def roll(self):
        # Simulate a dice roll and return a random integer between 1 and 6, inclusive.
        # This method uses Python's random module to generate the random number,
        # mimicking the behavior of a physical dice.
        return random.randint(1, 6)
