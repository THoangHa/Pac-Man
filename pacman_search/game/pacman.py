# game/pacman.py
"""
Pacman class represents the Pacman entity in the game.
Attributes:
    speed (int): The speed of the Pacman.
    directions (str): The current movement direction of the Pacman.
Methods:
    __init__(maze, position=(10, 10)):
        Initializes the Pacman with the given maze and position.
    handle_event(event):
        Handles the keyboard events to change the movement direction of the Pacman.
    update():
        Updates the state of the Pacman based on the current direction and moves it if the new position is not a wall.
"""

import pygame
from .entity import Entity
from .constants import TILE_SIZE, COLOUR_YELLOW, PACMAN_SPEED

class Pacman(Entity): # Represents the Pacman entity in the game
    def __init__(self, maze, position = (10, 10)): # Default position is (10, 10)
        super().__init__(
            maze, 
            position,
            colour = COLOUR_YELLOW,
            image_path = "assets/images/Entities/pacman.png"
        )
        self.speed = PACMAN_SPEED
        self.directions = None # Current movement direction

    def handle_event(self, event): # Handle the event
        if event.type == pygame.KEYDOWN: # If a key is pressed
            if event.key == pygame.K_UP:
                self.directions = 'UP'
            elif event.key == pygame.K_DOWN:
                self.directions = 'DOWN'
            elif event.key == pygame.K_LEFT:
                self.directions = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                self.directions = 'RIGHT'

    def update(self): # Update the state of the Pacman
        if self.directions: # If there is a direction
            row, col = self.position
            new_position = {
                'UP': (row - 1, col),
                'DOWN': (row + 1, col),
                'LEFT': (row, col - 1),
                'RIGHT': (row, col + 1)
            }[self.directions] # Get the new position based on the direction

            if not self.maze.is_wall(new_position): # If the new position is not a wall
                self.position = new_position