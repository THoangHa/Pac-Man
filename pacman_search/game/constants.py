# game/constants.py
"""
This module defines constants used throughout the Pacman game.
Constants:
    TILE_SIZE (int): The size of each tile in the game grid.
    MAZE_ROWS (int): The number of rows in the game maze.
    MAZE_COLS (int): The number of columns in the game maze.
    COLOUR_BLACK (tuple): RGB value for the color black.
    COLOUR_WHITE (tuple): RGB value for the color white.
    COLOUR_YELLOW (tuple): RGB value for the color yellow.
    PACMAN_SPEED (int): The speed of Pacman.
    GHOST_SPEED (int): The speed of the ghosts.
"""


TILE_SIZE = 32

# Maze Dimensions
MAZE_ROWS = 20
MAZE_COLS = 20

# Colours (RGB)
COLOUR_BLACK = (0, 0, 0)
COLOUR_WHITE = (255, 255, 255)
COLOUR_YELLOW = (255, 255, 0)
COLOUR_BLUE = (0, 0, 255)
COLOUR_ORANGE = (255, 165, 0)
COLOUR_PINK = (255, 192, 203)
COLOUR_RED = (255, 0, 0)


# Speeds
PACMAN_SPEED = 4
GHOST_SPEED = 2

