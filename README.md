# PigGame

Pig Dice Game 🎲

Welcome!

Greetings from the development team! We're thrilled to introduce our latest project, the Pig Dice Game, a Python-based rendition of the classic dice game. This project represents our collective effort to bring the fun and strategy of Pig into the digital realm, accessible right from your terminal.

Let's Get Started

Before You Begin

You'll need Python 3.6 or newer to play our game.

.  ⚙️ Set Up

First, clone our project repository:

git clone https://github.com/EmperorOlashinbo/PigGame.git

cd PigGame

cd src

Then, create and activate a virtual environment:

python -m venv venv

source venv/bin/activate on iOS & On Windows, use `venv\Scripts\activate`

Don't forget to install the required dependencies:

pip install -r requirements.txt or make install

.   Dive Into the Game 🎲

Launching the game is simple:

python Game1.py

Just follow the prompts to kick things off and enjoy the game with your friends or against our AI.

.   How We Play

The essence of the Pig Dice Game is risk management. Roll the dice to accumulate points, but be cautious—rolling a '1' resets your turn's score! You can choose to 'hold' at any point to secure your points. The game includes:

1. A single-player mode to challenge our crafty computer opponent.
2. A two-player mode for epic face-offs.
3. A high-score tracker to immortalize your victories.

.   📜 Game Rules

The Pig Dice Game is a fun and simple dice game that can be played with one or more players. Here are the basic rules:

1. Each player takes turns rolling a single six-sided die.
2. On their turn, a player can roll the die as many times as they want, accumulating points with each roll.
3. If a player rolls a 1, their turn ends immediately, and they lose all points accumulated during that turn.
4. Alternatively, a player can choose to "hold," which ends their turn and adds the points accumulated during that  turn to their total score.
5. The first player to reach or exceed 100 points wins the game.

.   Behind the Scenes

Collaborate With Us

We're always on the lookout for new ideas, improvements, or bug fixes. Feel free to dive into our code and contribute! Check out CONTRIBUTING.md for more on how to submit your contributions.

.   Test Like a Pro

We believe in the power of testing. Run the unit tests to ensure everything's in order:

python -m unittest

.   Style Matters

We adhere to PEP 8 standards for a clean, readable codebase. Use flake8 for style checks and black for automatic formatting:

flake8
black .

.   Docs and Diagrams

Feeling curious about the internals? Generate the documentation and UML diagrams:

make doc
make uml

Note: Graphviz needs to be set up for generating UML diagrams.

🐍 About the project

📝 The assignment

This is assignment 2 of Methods for Sustainable Programming course code DA115B VT24.
- This project was created and maintained by Ibrahim Olasunbo Ogunbanjo, MD Abu Taher and Shadman Intishar.
- Programming Language used: Python.

⚠️ Known issues

1. We prioritized the requirements to meet the second deadline.
2. We struggle for a week to be able to use the make command.
3. We also struggled to generate PDoc and UML diagrams, but we finally made it happen.

.   A Note on Licensing

Our project is open under the MIT License. See LICENSE.md for the full text.
