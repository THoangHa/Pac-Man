# game/ghosts/pink_ghost.py
"""
This module defines the PinkGhost class, which represents a pink ghost in the Pacman game.
Classes:
    PinkGhost: A class representing a pink ghost that uses Depth-First Search (DFS) to chase Pacman.
Methods:
    __init__(self, maze, start_pos):
        Initializes a PinkGhost instance with the given maze and starting position.
    compute_path(self, pacman_pos):
        Computes the path to chase Pacman using the DFS algorithm.
"""



from game.ghost import Ghost, ChasePacmanProblem
from search.DFS import DFS
from game.constants import COLOUR_PINK

class PinkGhost(Ghost): # PinkGhost class inherits from Ghost class
    """
    PinkGhost is a subclass of Ghost that represents the pink ghost in the Pacman game.
    Attributes:
        maze (Maze): The maze in which the ghost is located.
        position (tuple): The starting position of the ghost in the maze.
        colour (str): The colour of the ghost, set to pink.
        search_algorithm (SearchAlgorithm): The search algorithm used by the ghost to chase Pacman.
        path (list): The path computed by the search algorithm to chase Pacman.
    Methods:
        __init__(maze, start_pos):
            Initializes the PinkGhost with the given maze and starting position.
        compute_path(pacman_pos):
            Computes the path to chase Pacman using the search algorithm.
            Args:
                pacman_pos (tuple): The current position of Pacman in the maze.
            Returns:
                None
    """

    def __init__(self, maze, start_pos): #  method to initialize the PinkGhost instance
        super().__init__(
            maze, 
            position = start_pos,
            image_path = "assets\\images\\Entities\\pink_ghost.png",
        )
        self.search_algorithm = DFS()

    def compute_path(self, pacman_pos): # method to compute the path to chase Pacman
        problem = ChasePacmanProblem(self.maze, self.position, pacman_pos)
        result = self.search_algorithm.search(problem)
        self.path = result.actions if result.actions is not None else []