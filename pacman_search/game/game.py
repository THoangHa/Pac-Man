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
from game.ghosts.blue_ghost import BlueGhost
from game.ghosts.orange_ghost import OrangeGhost
from game.ghosts.pink_ghost import PinkGhost
from game.ghosts.red_ghost import RedGhost

class Game:
    def __init__(self, level = 1):
        pygame.init()
        
        self.level = level
        self.maze = Maze()
        
        # Example: Each level uses a different ghost or set of ghosts
        # Adjust as needed for your BFS, DFS, UCS, A* logic, etc.
        
        if level == 1:
            self.ghosts = [BlueGhost(self.maze, start_pos=(1, 1))]
        elif level == 2:
            self.ghosts = [PinkGhost(self.maze, start_pos=(1, self.maze.cols - 2))]
        elif level == 3:
            self.ghosts = [OrangeGhost(self.maze, start_pos=(self.maze.rows - 2, 1))]
        elif level == 4:
            self.ghosts = [RedGhost(self.maze, start_pos=(self.maze.rows - 2, self.maze.cols - 2))]
        elif level == 5:
            self.ghosts = [
                BlueGhost(self.maze, start_pos=(1, 1)),
                PinkGhost(self.maze, start_pos=(1, self.maze.cols - 2)),
                OrangeGhost(self.maze, start_pos=(self.maze.rows - 2, 1)),
                RedGhost(self.maze, start_pos=(self.maze.rows - 2, self.maze.cols - 2))
            ]
        elif level == 6: # Will be modified in the future
            # Possibly a special mode or advanced logic
            # For demonstration, reuse all ghosts but do something special
            self.ghosts = [
                BlueGhost(self.maze, start_pos=(1, 1)),
                PinkGhost(self.maze, start_pos=(1, self.maze.cols - 2)),
                OrangeGhost(self.maze, start_pos=(self.maze.rows - 2, 1)),
                RedGhost(self.maze, start_pos=(self.maze.rows - 2, self.maze.cols - 2))
            ]
        
        self.width = self.maze.cols * TILE_SIZE
        self.height = self.maze.rows * TILE_SIZE
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Pac-Man
        self.pacman = Pacman(self.maze, position = (10, 10))
        self.clock = pygame.time.Clock()

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
        