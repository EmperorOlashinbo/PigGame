import unittest
from unittest.mock import MagicMock, patch
import builtins
from Game1 import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        # Mock the built-in input function to control user inputs
        self.mock_input = MagicMock()
        builtins.input = self.mock_input

    def test_setup_two_players(self):
        # Test setup for two players without AI
        self.mock_input.side_effect = ["2", "Player1", "Player2", "n"]
        game = Game()
        self.assertEqual(len(game.players), 2)  # Expecting two players to be setup

    def test_setup_single_player_without_ai(self):
        # Test setup for one player without including an AI
        self.mock_input.side_effect = ["1", " ", "n"]
        game = Game()
        self.assertEqual(len(game.players), 1)
        self.assertNotIn("Computer", [player.name for player in game.players])

    @patch("builtins.print")
    def test_player_turns(self, mock_print):
        # Test the turn-taking logic to ensure proper scoring and turn cycling
        game = Game()
        for _ in range(10):
            current_player = game.players[game.current_player_index]
            initial_score = current_player.score
            game.play_turn(current_player)
            # Check if game correctly cycles to the next player when a player scores over 100
            if current_player.score >= 100:
                self.assertEqual(game.current_player_index, 0)  # Assuming the game should cycle back to the first player

    @patch("builtins.input")
    @patch("builtins.print")
    def test_play_game_termination(self, mock_print, mock_input):
        # Simulate a game where players reach the score threshold to end the game
        mock_input.side_effect = ["2", "Player1", "Player2", "n"]
        game = Game()
        game.players[0].score = 95  # Setting scores near 100 to test game end condition
        game.players[1].score = 90

        with patch.object(Game, "play_turn", autospec=True) as mock_play_turn:
            # Simulate turn behavior for automatic score increment
            mock_play_turn.side_effect = lambda self, player: setattr(player, 'score', player.score + 5)
            game.play_game()

        # Ensure game ends when a player's score reaches 100 or more
        self.assertTrue(any(player.score >= 100 for player in game.players))
        # Check output for winning message
        winning_player = next(player for player in game.players if player.score >= 100)
        mock_print.assert_any_call(f"\n{winning_player.name} wins with a score of {winning_player.score}!")

        # Confirm high scores and histogram outputs
        mock_print.assert_any_call("\nHigh Scores:")
        mock_print.assert_any_call("\nDice Roll Histogram:")

if __name__ == "__main__":
    unittest.main()
