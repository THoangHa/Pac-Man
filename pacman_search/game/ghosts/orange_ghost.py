# game/ghosts/orange_ghost.py
"""
This module defines the OrangeGhost class, which represents an orange ghost in the Pacman game.
Classes:
    OrangeGhost: A subclass of Ghost that uses the Uniform Cost Search (UCS) algorithm to chase Pacman.
Methods:
    __init__(self, maze, start_pos):
        Initializes an OrangeGhost instance with the given maze and starting position.
    compute_path(self, pacman_pos):
        Computes the path to chase Pacman using the UCS algorithm.
"""


from game.ghost import Ghost, ChasePacmanProblem
from search.UCS import UCS
from game.constants import COLOUR_ORANGE

class OrangeGhost(Ghost): # OrangeGhost class inherits from Ghost class
    """
    Represents the orange ghost in the Pacman game, inheriting from the Ghost class.
    Attributes:
        maze (Maze): The maze in which the ghost is located.
        position (tuple): The starting position of the ghost.
        colour (str): The colour of the ghost, set to COLOUR_ORANGE.
        search_algorithm (SearchAlgorithm): The search algorithm used by the ghost to chase Pacman.
    Methods:
        __init__(maze, start_pos):
            Initializes the OrangeGhost with the given maze and starting position.
        compute_path(pacman_pos):
            Computes the path to chase Pacman using the specified search algorithm.
            Args:
                pacman_pos (tuple): The current position of Pacman.
            Returns:
                None
    """

    def __init__(self, maze, start_pos): # method to initialize the OrangeGhost instance
        super().__init__(
            maze, 
            position = start_pos,
            image_path = "assets\\images\\Entities\\orange_ghost.png",
        )
        self.search_algorithm = UCS()

    def compute_path(self, pacman_pos): # method to compute the path to chase Pacman
        problem = ChasePacmanProblem(self.maze, self.position, pacman_pos)
        result = self.search_algorithm.search(problem)
        self.path = result.actions if result.actions is not None else []