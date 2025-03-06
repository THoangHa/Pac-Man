# game/ghosts/red_ghost.py
"""
This module defines the RedGhost class, which represents the red ghost in the Pacman game.
Classes:
    RedGhost: A subclass of Ghost that uses the A* search algorithm to chase Pacman.
Methods:
    __init__(self, maze, start_pos):
        Initializes a RedGhost instance with the given maze and starting position.
    compute_path(self, pacman_pos):
        Computes the path to chase Pacman using the A* search algorithm.
"""



from game.ghost import Ghost, ChasePacmanProblem
from search.AStar import AStar
from game.constants import COLOUR_RED

class RedGhost(Ghost): # RedGhost class inherits from Ghost class
    class RedGhost(Ghost):
        """
        RedGhost class represents the red ghost in the Pacman game, inheriting from the Ghost class.
        Attributes:
            maze (Maze): The maze in which the ghost is located.
            position (tuple): The starting position of the ghost in the maze.
            colour (str): The colour of the ghost, set to red.
            search_algorithm (SearchAlgorithm): The algorithm used to compute the path to chase Pacman.
        Methods:
            __init__(maze, start_pos):
                Initializes the RedGhost instance with the given maze and starting position.
            compute_path(pacman_pos):
                Computes the path to chase Pacman using the A* search algorithm.
                Args:
                    pacman_pos (tuple): The current position of Pacman in the maze.
                Returns:
                    None
        """
    
    def __init__(self, maze, start_pos): # method to initialize the RedGhost instance
        super().__init__(
            maze, 
            position = start_pos,
            image_path = "assets\\images\\Entities\\red_ghost.png",
        )
        self.search_algorithm = AStar()

    def compute_path(self, pacman_pos): # method to compute the path to chase Pacman
        problem = ChasePacmanProblem(self.maze, self.position, pacman_pos)
        result = self.search_algorithm.search(problem)
        self.path = result.actions if result.actions is not None else []