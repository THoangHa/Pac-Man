# gui/game_screen.py
"""
This module defines the GameScreen class which handles the display and interaction
of the game screen using the Pygame library.
Classes:
    GameScreen: Manages the game screen, initializes the game, and handles events.
Methods:
    __init__(self, screen):
        Initializes the GameScreen with the given screen and sets up the game instance.
    run(self):
        Runs the game loop and handles events such as quitting the game or returning to the menu.
"""



import pygame
from game.game import Game

class GameScreen:
    def __init__(self, screen, level):
        self.screen = screen
        self.level = level
        self.game = Game(level = self.level)
        self.game.screen = screen

    def run(self):
        self.game.run()
        # Check for events to return to menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return