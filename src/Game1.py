from Dice import Dice
from Player import Player
from DiceHand import DiceHand
from Histogram import Histogram
from Intelligence import Intelligence
from HighScores import HighScores

class Game:
    def __init__(self):
        # Initialize components of the game, including dice, players, and high scores.
        self.dice = Dice()
        self.players = self.setup_players()  # Set up human and possibly AI players.
        self.current_player_index = 0  # Track whose turn it is to play.
        self.high_scores = HighScores()  # High scores manager.
        self.histogram = Histogram()  # Record and display roll statistics.
        self.ai = None  # AI intelligence, initialized only if playing against the computer.

    def setup_players(self):
        # Setup the game players based on user input for number of players and names.
        players = []
        number_of_players = int(input("Enter the number of human players (1 for single player, 2 or more for multiplayer): "))
        for i in range(number_of_players):
            name = input(f"Enter player {i + 1} name: ")
            players.append(Player(name))

        # If there is only one human player, ask if they want to play against the computer.
        if number_of_players == 1:
            include_computer = input("Do you want to include a computer opponent? (y/n): ").strip().lower() == "y"
            if include_computer:
                ai_difficulty = input("Select AI difficulty (easy, medium, hard): ").strip().lower()
                self.ai = Intelligence(level=ai_difficulty)
                players.append(Player("Computer"))

        return players

    def play_turn(self, player):
        # Manage a single turn for one player: roll dice, update scores, and decide whether to continue.
        turn_score = 0
        dice_hand = DiceHand()

        while True:
            roll = self.dice.roll()
            dice_hand.add_roll(roll)
            self.histogram.add(roll)

            print(f"{player.name} rolled a {roll}")
            if roll == 1:
                print("Oops! Rolled a 1. No points this turn.")
                break
            else:
                turn_score += roll
                print(f"Turn score: {turn_score}, Total score if held: {player.score + turn_score}")

                if player.name == "Computer" and self.ai:
                    if not self.ai.should_roll_again(player.score, turn_score):
                        print("Computer decides to hold.")
                        break
                else:
                    choice = input("Roll again? (y/n): ").strip().lower()
                    if choice != 'y':
                        break

        player.update_score(turn_score)

    def play_game(self):
        # Begin and manage the entire game, prompting each player's turn until a winner emerges.
        print("Welcome to the Pig Dice Game!")
        while True:
            current_player = self.players[self.current_player_index]
            print(f"\n{current_player.name}'s turn. Current score: {current_player.score}")
            self.play_turn(current_player)

            if current_player.score >= 100:
                print(f"\n{current_player.name} wins with a score of {current_player.score}!")
                self.high_scores.save_score(current_player.name, current_player.score)
                break

            self.current_player_index = (self.current_player_index + 1) % len(self.players)

        print("\nHigh Scores:")
        self.high_scores.display()

        print("\nDice Roll Histogram:")
        self.histogram.display()

if __name__ == "__main__":
    game = Game()
    game.play_game()
