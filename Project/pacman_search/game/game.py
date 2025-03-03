# game/game.py
"""
This module contains the Game class which initializes and runs the Pac-Man game.
Classes:
    Game: Manages the game loop, event handling, updating, and rendering of game entities.
Methods:
    __init__: Initializes the game, including the maze, screen, clock, Pac-Man, and ghosts.
    run: Runs the main game loop, handling events, updating game state, and rendering.
    handle_events: Handles user input and other events.
    update: Updates the game state, including the positions of Pac-Man and the ghosts.
    render: Renders the game entities on the screen.
"""

import pygame
import sys
from .constants import TILE_SIZE, COLOUR_BLACK
from .maze import Maze
from .pacman import Pacman
from .ghost.blue_ghost import BlueGhost
from .ghost.orange_ghost import OrangeGhost
from .ghost.pink_ghost import PinkGhost
from .ghost.red_ghost import RedGhost

class Game:
    def __init__(self):
        pygame.init()
        self.maze = Maze()
        self.width = self.maze.cols * TILE_SIZE
        self.height = self.maze.rows * TILE_SIZE
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Pac-Man')
        self.clock = pygame.time.Clock()

        # Initialize the game entities
        self.pacman = Pacman(self.maze, position=(10, 10))

        self.ghosts = [
            BlueGhost(self.maze, position=(1, 1)),
            OrangeGhost(self.maze, position=(1, 18)),
            PinkGhost(self.maze, position=(18, 1)),
            RedGhost(self.maze, position=(18, 18))
        ]

    def run(self): # Run the game loop
        while True:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(10) # Limit the frame rate to 10 FPS

    def handle_events(self): # Handle events in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.pacman.handle_event(event) # Handle events for the Pacman

    def update(self): # Update the game state for the entities in the game loop
        self.pacman.update()
        pacman_position = self.pacman.position

        ghost_positions = [ghost.position for ghost in self.ghosts]
        for ghost in self.ghosts:
            ghost.update(pacman_position, ghost_positions)

    
    def render(self): # Render the game entities on the screen
        self.screen.fill(COLOUR_BLACK)
        self.maze.render(self.screen)
        self.pacman.render(self.screen)
        for ghost in self.ghosts:
            ghost.render(self.screen)

        pygame.display.flip()

    if __name__ == '__main__': # Run the game
        game = Game()
        game.run()
        