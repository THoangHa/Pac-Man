#search/__init__.py
"""
This module initializes the search package and imports various search-related classes and functions.
Imports:
    - SearchProblem: A class representing a search problem.
    - SearchAlgorithm: A base class for search algorithms.
    - SearchResult: A class representing the result of a search.
    - reconstruct_path: A function to reconstruct the path from the search result.
    - Node: A class representing a node in the search tree.
    - PriorityQueue: A class representing a priority queue.
    - null_heuristic: A heuristic function that always returns zero.
    - BFS: A class implementing the Breadth-First Search algorithm.
    - DFS: A class implementing the Depth-First Search algorithm.
    - UCS: A class implementing the Uniform Cost Search algorithm.
    - AStar: A class implementing the A* Search algorithm.
"""

from .Search import SearchProblem, SearchAlgorithm, SearchResult, reconstruct_path
from .utils import Node, PriorityQueue, null_heuristic
from .BFS import BFS
from .DFS import DFS
from .UCS import UCS
from .AStar import AStar