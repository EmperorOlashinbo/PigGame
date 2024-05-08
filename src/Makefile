# Makefile for the Dice Game project

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
all: install lint format test coverage doc uml

# Install dependencies
install:
    @echo "Installing dependencies..."
    $(PIP) install -r requirements.txt

# Run flake8
flake8:
    @echo "Linting code with Flake8..."
    $(FLAKE8) dice_game1.py test_dice.py.

# Run pylint
pylint:
    @echo "Linting code with Pylint..."
    $(PYLINT) dice_game1.py test_dice.py

# Run linters
lint:
    @echo "Running linters..."
    $(FLAKE8) dice_game1.py test_dice.py
    $(PYLINT) dice_game1.py test_dice.py

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
    $(PYTEST) --cov-report term --cov=dice_game1.py test_dice.py

# Generate documentation
doc:
    @echo "Generating documentation..."
    $(SPHINX_BUILD) -b html doc/source doc/build

# Generate UML diagrams
uml:
    @echo "Generating UML diagrams..."
    $(PYREVERSE) -o png -p DiceGame dice_game1.py
    mv *.png doc/uml/

# Clean up
clean:
    @echo "Cleaning up..."
    find . -type f -name '*.pyc' -delete
    find . -type d -name '__pycache__' -delete
    rm -rf .pytest_cache
    rm -rf doc/build
    rm -rf doc/uml/*.png

.PHONY: all install lint black test coverage doc uml clean flake8 pylint