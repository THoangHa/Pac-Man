# game/ghost.py
"""
This module defines the behavior of ghosts in the Pacman game.
Classes:
    ChasePacmanProblem: A search problem for chasing Pacman.
    Ghost: Represents a ghost entity in the game.
ChasePacmanProblem:
    Methods:
        __init__(maze, start, goal): Initializes the problem with the maze, start, and goal positions.
        get_initial_state(): Returns the initial state of the problem.
        goal_test(state): Checks if the given state is the goal state.
        get_successors(state): Returns the successors of the given state.
        heuristic(state): Computes the heuristic value for the given state using Manhattan distance.
Ghost:
    Methods:
        __init__(maze, position, colour, speed): Initializes the ghost with the maze, position, color, and speed.
        update(pacman_pos, other_ghosts_positions): Updates the state of the ghost based on Pacman's position and other ghosts' positions.
        get_new_position(move): Returns the new position of the ghost based on the given move.
        compute_path(pacman_pos): Computes the path to Pacman's position (to be implemented by subclasses).
"""



from .entity import Entity
from search import SearchProblem
from search.utils import null_heuristic
from .constants import GHOST_SPEED

class ChasePacmanProblem(SearchProblem):
    def __init__(self, maze, start, goal): # Initialize the problem
        self.maze = maze
        self.start = start
        self.goal = goal

    def get_initial_state(self): # Get the initial state
        return self.start 

    def goal_test(self, state): # Check if the state is the goal state
        return state == self.goal

    def get_successors(self, state): # Get the successors of the state
        return self.maze.get_neighbours(state) # Delegate to the maze for valid neighbour moves

    def heuristic(self, state):
        # Use Manhattan distance as heuristic
        row, col = state
        goal_row, goal_col = self.goal
        return abs(row - goal_row) + abs(col - goal_col)

class Ghost(Entity): # Represents a ghost entity in the game
    def __init__(
        self, 
        maze, 
        position = (0, 0), 
        colour = (255, 0, 0),
        speed = GHOST_SPEED,
        image_path = None
    ):
        super().__init__(maze, position, colour, image_path)
        self.speed = speed
        self.path = [] # List of actions to reach the target

    def update(self, pacman_pos, other_ghosts_positions): # Update the state of the ghost
        if not self.path: # If there is no path
            self.compute_path(pacman_pos)

        if self.path: # If there is a path
            next_move = self.path.pop(0)
            new_position = self.get_new_position(next_move)
            if not self.maze.is_wall(new_position) and new_position not in other_ghosts_positions: # Check if the new position is not a wall and not occupied by another ghost
                self.position = new_position

    def get_new_position(self, move):
        row, col = self.position
        if move == 'UP':
            return (row - 1, col)
        elif move == 'DOWN':
            return (row + 1, col)
        elif move == 'LEFT':
            return (row, col - 1)
        elif move == 'RIGHT':
            return (row, col + 1)
        
        return self.position

    def compute_path(self, pacman_pos): # Compute the path to the pacman
        raise NotImplementedError("This method should be implemented by the subclass")
       