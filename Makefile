# Makefile for the Pig Dice Game project

# Variables
VENV = venv
PYTHON = $(VENV)/Scripts/python
PIP = $(VENV)/Scripts/pip
PYTEST = $(VENV)/Scripts/pytest
FLAKE8 = $(VENV)/Scripts/flake8
PYLINT = $(VENV)/Scripts/pylint
BLACK = $(VENV)/Scripts/black
SPHINX_BUILD = $(VENV)/Scripts/sphinx-build
PYREVERSE = $(VENV)/Scripts/pyreverse

# Default target
all: install lint black test coverage doc uml

# Install dependencies
install:
	@echo "Installing dependencies..."
	$(PIP) install -r requirements.txt

# Run flake8
flake8:
	@echo "Linting code with Flake8..."
	$(FLAKE8) 

# Run pylint
pylint:
	@echo "Linting code with Pylint..."
	$(PYLINT) 

# Run linters
lint:
	@echo "Running linters..."
	$(FLAKE8) 
	$(PYLINT) 

# Format code with Black
black:
	@echo "Formatting code with Black..."
	$(BLACK) .

# Run tests
test:
	@echo "Running tests..."
	$(PYTEST)

# Generate coverage report
coverage:
	@echo "Generating coverage report..."
	$(PYTEST) --cov-report term --cov=Dice.py Game1.py HighScores.py Intelligence.py Histogram.py 
	DiceHand.py Player.py TestGame.py TestHighScores.py Player.py TestGame.py TestIntelligence.py 
	TestHistogram.py TestDiceHand.py TestPlayer.py TestDice.py

# Generate documentation
doc: pdoc pyreverse
	@echo "Generating documentation..."
	$(SPHINX_BUILD) -b html doc/source doc/build Dice.py Game1.py HighScores.py Intelligence.py 
	Histogram.py DiceHand.py Player.py TestGame.py TestHighScores.py Player.py TestGame.py 
	TestIntelligence.py TestHistogram.py TestDiceHand.py TestPlayer.py TestDice.py

# Generate UML diagrams
uml:
	@echo "Generating UML diagrams..."
	$(PYREVERSE) -o png -p DiceGame Dice.py Game1.py HighScores.py Intelligence.py Histogram.py 
	DiceHand.py Player.py TestGame.py TestHighScores.py Player.py TestGame.py TestIntelligence.py 
	TestHistogram.py TestDiceHand.py TestPlayer.py TestDice.py
	mv *.png doc/uml/

# Clean up
clean:
	@echo "Cleaning up..."
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf .pytest_cache
	rm -rf doc/build
	rm -rf doc/uml/*.png

# Calculate software metrics for your project.

radon-cc:
	@$(call MESSAGE,$@)
	radon cc --show-complexity --average pig

radon-mi:
	@$(call MESSAGE,$@)
	radon mi --show pig

radon-raw:
	@$(call MESSAGE,$@)
	radon raw pig

radon-hal:
	@$(call MESSAGE,$@)
	radon hal pig

cohesion:
	@$(call MESSAGE,$@)
	cohesion --directory pig

metrics: radon-cc radon-mi radon-raw radon-hal cohesion

bandit:
	@$(call MESSAGE,$@)
	bandit --recursive pig

.PHONY: all install lint black test coverage doc uml clean flake8 pylint
