# game/ghosts/pink_ghost.py
"""
This module defines the BlueGhost class, which represents a blue ghost in the Pacman game.
Classes:
    BlueGhost: A subclass of Ghost that uses BFS to chase Pacman.
Methods:
    __init__(self, maze, start_pos):
        Initializes a BlueGhost instance with the given maze and starting position.
    compute_path(self, pacman_pos):
        Computes the path to chase Pacman using BFS algorithm.
"""

from game.ghost import Ghost, ChasePacmanProblem
from search.BFS import BFS
from game.constants import COLOUR_BLUE


class BlueGhost(Ghost): # BlueGhost class inherits from Ghost class
    """
    BlueGhost is a subclass of Ghost that represents the blue ghost in the Pacman game.
    It uses the Breadth-First Search (BFS) algorithm to chase Pacman.
    Attributes:
        maze (Maze): The maze in which the ghost is moving.
        position (tuple): The current position of the ghost in the maze.
        colour (str): The colour of the ghost.
        search_algorithm (SearchAlgorithm): The search algorithm used to compute the path to Pacman.
        path (list): The list of actions to reach Pacman.
    Methods:
        __init__(maze, start_pos):
            Initializes the BlueGhost with the given maze and starting position.
        compute_path(pacman_pos):
            Computes the path to the given Pacman position using the BFS algorithm.
    """

    def __init__(self, maze, start_pos): # method to initialize the BlueGhost instance
        super().__init__(
            maze, 
            position = start_pos,
            image_path = "assets\\images\\Entities\\blue_ghost.png",
        )
        self.search_algorithm = BFS()

    def compute_path(self, pacman_pos): # method to compute the path to chase Pacman
        problem = ChasePacmanProblem(self.maze, self.position, pacman_pos)
        result = self.search_algorithm.search(problem)
        self.path = result.actions if result.actions is not None else[]