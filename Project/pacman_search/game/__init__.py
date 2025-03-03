# game/__init__.py
"""
This module initializes the game package by importing the necessary classes.
Classes:
    Game: Represents the main game logic and controls.
    Maze: Represents the maze structure of the game.
    Entity: Represents a generic entity in the game.
    Pacman: Represents the Pacman character.
    Ghost: Represents the ghost characters.
Modules:
    game: Contains the Game class.
    maze: Contains the Maze class.
    entity: Contains the Entity class.
    pacman: Contains the Pacman class.
    ghost: Contains the Ghost class.
"""



from .game import Game
from .maze import Maze
from .entity import Entity
from .pacman import Pacman
from .ghost import Ghost