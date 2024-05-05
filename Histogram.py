class Histogram:
    def __init__(self):
        # Initialize a dictionary to store the frequency of each dice roll.
        self.data = {}

    def add(self, roll):
        # Increment the count for a specific dice roll in the histogram.
        # If the roll is not yet in the dictionary, it starts with a count of 0 before adding 1.
        self.data[roll] = self.data.get(roll, 0) + 1

    def display(self):
        # Print the histogram sorted by roll number.
        # Each roll is displayed with a number of asterisks corresponding to its frequency.
        for roll in sorted(self.data):
            print(f"{roll}: {'*' * self.data[roll]}")
