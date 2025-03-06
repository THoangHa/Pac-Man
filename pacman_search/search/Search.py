# search/Search.py 
"""
This module defines the abstract base classes for search problems and search algorithms, 
as well as utility functions and data structures for search.
Classes:
    SearchProblem: An abstract base class for defining search problems.
    SearchAlgorithm: An abstract base class for defining search algorithms.
    SearchResult: A data class for storing the results of a search.
Functions:
    reconstruct_path(node): Reconstructs the path from the initial state to the given node.
Classes and Methods:
    SearchProblem:
        get_initial_state(): Returns the initial state of the problem.
        get_successors(state): Returns the successors of the given state.
        get_cost(current_cost, step_cost): Returns the total cost after taking a step.
        heuristic(state): Returns the heuristic value of the given state.
        goal_test(state): Checks if the given state is the goal state.
    SearchAlgorithm:
        search(problem: SearchProblem) -> Optional[List[Any]]: Performs a search to find a solution to the given search problem.
"""

import abc
from dataclasses import dataclass
from typing import List, Optional, Any

class SearchProblem(abc.ABC):

    @abc.abstractmethod
    def get_initial_state(self):
        pass # return the initial state of the problem

    @abc.abstractmethod
    def get_successors(self, state):
        pass


    def get_cost(self, current_cost, step_cost):
        return current_cost + step_cost

    def heuristic(self, state):
        return 0

    @abc.abstractmethod
    def goal_test(self, state):
        pass


class SearchAlgorithm(abc.ABC):
    @abc.abstractmethod
    def search(self, problem: SearchProblem) -> Optional[List[Any]]:
        """
        Perform a search to find a solution to the given search problem.
        Args:
            problem (SearchProblem): The search problem to solve.
        Returns:
            Optional[List[Any]]: A list of actions that represents the solution to the problem, 
                                 or None if no solution is found.
        """

        pass


def reconstruct_path(node):
    actions = []
    while node.parent is not None:
        actions.append(node.action)
        node = node.parent
    actions.reverse()
    return actions

@dataclass
class SearchResult:
    actions: Optional[List[Any]]
    search_time: float
    memory_usage: float
    nodes_expanded: int