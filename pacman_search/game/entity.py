# game/entity.py
"""
Entity class represents a game entity in the Pacman game.
Attributes:
    maze: The maze in which the entity exists.
    position: A tuple representing the (row, col) position of the entity in the maze.
    colour: The colour of the entity.
Methods:
    __init__(maze, position, colour):
        Initializes the Entity with a maze, position, and colour.
    update():
        Updates the state of the entity. This method should be overridden by subclasses.
    render(screen):
        Renders the entity on the given screen.
"""


import pygame
from .constants import TILE_SIZE, COLOUR_WHITE

class Entity: # Base class for all entities in the game
    def __init__(self, maze, position = (0, 0), colour = (255, 255, 255), image_path = None): # Default position is (0, 0) and default colour is white
        self.maze = maze
        self.position = position
        self.colour = colour
        self.image = None

        if image_path:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
    
    def update(self): # This method should be overridden by subclasses
        pass

    def render(self, screen): # This method should be overridden by subclasses
        row, col = self.position
        x = col * TILE_SIZE
        y = row * TILE_SIZE
        
        if self.image:
            screen.blit(self.image, (x, y))
        else:
            # Fallback: draw a colored rectangle or circle
            rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, self.color, rect)