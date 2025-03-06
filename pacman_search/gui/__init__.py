# gui/__init__.py
"""
This module initializes the GUI components for the Pacman search project.
It imports the following components:
- Menu: The main menu of the game.
- GameScreen: The screen where the game is played.
- Leaderboard: The leaderboard screen displaying high scores.
- LevelSelect: The screen for selecting game levels.
- utils: Utility functions and classes for the GUI, including:
    - load_font: Function to load fonts.
    - draw_text: Function to draw text on the screen.
    - Button: A class representing a clickable button.
"""



from .menu import Menu
from .game_screen import GameScreen
from .leaderboard import Leaderboard
from .level_select import LevelSelect
from .utils import load_font, draw_text, Button
