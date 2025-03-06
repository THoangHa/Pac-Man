# game/maze.py

import os
import pygame
from .constants import TILE_SIZE, MAZE_ROWS, MAZE_COLS
import sys

class Maze: # Represents the maze in the game
    def __init__(self): # Initialize the maze
        self.rows = MAZE_ROWS
        self.cols = MAZE_COLS
        self.grid = self.generate_maze()
        
        # # Load the images for the maze
        # self.wall_image_h = pygame.image.load("assets\images\map_images\horizontal_walls.png").convert_alpha()  
        # self.wall_image_h = pygame.transform.scale(self.wall_image_h, (TILE_SIZE, TILE_SIZE))

        # self.wall_image_v = pygame.image.load("assets\images\map_images\vertical_walls.png").convert_alpha()
        # self.wall_image_v = pygame.transform.scale(self.wall_image_v, (TILE_SIZE, TILE_SIZE))

        # self.empty_image = pygame.image.load("assets\images\map_images\empty.png").convert_alpha()
        # self.empty_image = pygame.transform.scale(self.empty_image, (TILE_SIZE, TILE_SIZE))

        # self.blue_dot_image = pygame.image.load("assets\images\map_images\blue_dot.png").convert_alpha()
        # self.blue_dot_image = pygame.transform.scale(self.dot_image, (TILE_SIZE, TILE_SIZE))

        # Use os.path.join for cross-platform compatibility
        base_path = os.path.join('assets', 'images', 'map_images')
        
        # Error handling for image loading
        try:
            # Horizontal walls
            self.wall_image_h = pygame.image.load(os.path.join(base_path, 'horizontal_walls.png')).convert_alpha()
            self.wall_image_h = pygame.transform.scale(self.wall_image_h, (TILE_SIZE, TILE_SIZE))

            # Vertical walls
            self.wall_image_v = pygame.image.load(os.path.join(base_path, 'vertical_walls.png')).convert_alpha()
            self.wall_image_v = pygame.transform.scale(self.wall_image_v, (TILE_SIZE, TILE_SIZE))

            # Empty tile
            self.empty_image = pygame.image.load(os.path.join(base_path, 'empty.png')).convert_alpha()
            self.empty_image = pygame.transform.scale(self.empty_image, (TILE_SIZE, TILE_SIZE))

            # Blue dot
            self.blue_dot_image = pygame.image.load(os.path.join(base_path, 'blue_dot.png')).convert_alpha()
            self.blue_dot_image = pygame.transform.scale(self.blue_dot_image, (TILE_SIZE, TILE_SIZE))

            # Regular dot
            self.dot_image = pygame.image.load(os.path.join(base_path, 'blue_dot.png')).convert_alpha()
            self.dot_image = pygame.transform.scale(self.dot_image, (TILE_SIZE, TILE_SIZE))
        
        except pygame.error as e:
            print(f"Error loading maze images: {e}")
            # Provide fallback images or exit
            sys.exit(1)

    def generate_maze(self):
        # Create a grid with a wall border and simple internal walls
        grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)] # 0 is a path, 1 is a wall
        for i in range(self.rows):
            grid[i][0] = grid[i][self.cols - 1] = 1 # Create left and right walls
        for j in range(self.cols):
            grid[0][j] = grid[self.rows - 1][j] = 1 # Create top and bottom walls

        # Create internal walls
        for i in range(2, self.rows - 2, 2): # Skip every other row
            for j in range(2, self.cols - 2, 2): # Skip every other column
                grid[i][j] = 1

        return grid

    def is_wall(self, pos): # pos is a tuple (row, col)
        row, col = pos 
        return self.grid[row][col] == 1
        
    def get_neighbours(self, pos): # pos is a tuple (row, col)
        row, col = pos
        directions = {
            'UP': (-1, 0),
            'DOWN': (1, 0),
            'LEFT': (0, -1),
            'RIGHT': (0, 1)
        }

        neighbours = [] # List of tuples (action, new_pos, cost)
        for action, (dr, dc) in directions.items():
            new_pos = (row + dr, col + dc)
            if 0 <= new_pos[0] < self.rows and 0 <= new_pos[1] < self.cols:
                neighbours.append((action, new_pos, 1)) # 1 is the cost to move to a neighbour 

        return neighbours

    def is_intersection(self, row, col): # Check if the cell is an intersection
        if self.grid[row][col] != 0:
            return False
        
        # Check top-left corner
        if row > 0 and col > 0 and self.grid[row - 1][col] == 1 and self.grid[row][col - 1] == 1:
            return True
        # Check top-right corner
        if row > 0 and col < self.cols - 1 and self.grid[row - 1][col] == 1 and self.grid[row][col + 1] == 1:
            return True
        # Check bottom-left corner
        if row < self.rows - 1 and col > 0 and self.grid[row + 1][col] == 1 and self.grid[row][col - 1] == 1:
            return True
        # Check bottom-right corner
        if row < self.rows - 1 and col < self.cols - 1 and self.grid[row + 1][col] == 1 and self.grid[row][col + 1] == 1:
            return True
        
        return False

    def render(self, screen): # Render the maze on the screen
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * TILE_SIZE
                y = row * TILE_SIZE
                if self.grid[row][col] == 1:
                    # Choose wall tile based on position
                    if row == 0 or row == self.rows - 1:
                        screen.blit(self.wall_image_h, (x, y))
                    elif col == 0 or col == self.cols - 1:
                        screen.blit(self.wall_image_v, (x, y))
                    else:
                        # For internal walls, default to horizontal wall image.
                        screen.blit(self.wall_image_h, (x, y))
                else:
                    # Draw the empty cell background
                    screen.blit(self.empty_image, (x, y))
                    
                    # Determine which dot to render:
                    # Use blue dot if the cell is an intersection/corner; otherwise use the normal dot.
                    dot = self.blue_dot_image if self.is_intersection(row, col) else self.dot_image
                    
                    dot_w, dot_h = dot.get_size()
                    pos_x = x + (TILE_SIZE - dot_w) // 2
                    pos_y = y + (TILE_SIZE - dot_h) // 2
                    screen.blit(dot, (pos_x, pos_y))