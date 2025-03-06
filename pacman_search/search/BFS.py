#search/BFS.py
"""
Breadth-First Search (BFS) algorithm implementation.
This module contains the BFS class, which inherits from the SearchAlgorithm class and implements the search method to solve search problems using the Breadth-First Search strategy.
Classes:
    BFS: Implements the BFS search algorithm.
Methods:
    search(problem):
        Performs the BFS search on the given problem.
        Args:
            problem: An instance of a search problem that provides the initial state, goal test, and successor function.
        Returns:
            SearchResult: An object containing the actions to reach the goal, search time, memory usage, and nodes expanded.
"""

import time # for time usage
import tracemalloc # for memory usage
from collections import deque
from .Search import SearchAlgorithm, reconstruct_path, SearchResult
from .utils import Node


class BFS(SearchAlgorithm):
    """
    Breadth-First Search (BFS) algorithm implementation for solving search problems.
    Methods
    -------
    search(problem):
        Performs the BFS algorithm to find the solution to the given problem.
    """
    """
        Perform a breadth-first search to solve the given problem.
        Parameters
        ----------
        problem : Problem
            The problem to be solved, which must provide methods get_initial_state(), get_successors(state), and goal_test(state).
        Returns
        -------
        SearchResult
            An object containing the following attributes:
            - actions: List of actions to reach the goal state, or None if no solution is found.
            - search_time: Time taken to perform the search.
            - memory_usage: Peak memory usage during the search.
            - nodes_expanded: Number of nodes expanded during the search.
    """

    def search(self, problem):
        start_time = time.perf_counter()
        tracemalloc.start()
        nodes_expanded = 0

        intial_state = problem.get_initial_state()
        # Create the root node
        root = Node(state = intial_state, parent = None, action = None, path_cost = 0)

        # Check if the root node is the goal state
        if problem.goal_test(root.state): # if the root is the goal state
            end_time = time.perf_counter() # get the end time
            current, peak = tracemalloc.get_traced_memory() # get the current memory usage
            tracemalloc.stop() # stop the memory usage

            return SearchResult( # return the search result
                actions = reconstruct_path(root),
                search_time = end_time - start_time,
                memory_usage = peak,
                nodes_expanded = nodes_expanded
            )

        frontier = deque([root]) # create a deque with the root node
        explored = set([root.state]) # create a set with the root state

        while frontier: # while the frontier is not empty
            node = frontier.popleft()
            nodes_expanded += 1

            for action, next_state, cost in problem.get_successors(node.state): # get the successors of the node
                if next_state not in explored:
                    child = Node(
                        state = next_state,
                        parent = node,
                        action = action,
                        path_cost = node.path_cost + cost
                    )

                    if problem.goal_test(child.state): # if the child is the goal state
                        end_time = time.perf_counter()
                        current, peak = tracemalloc.get_traced_memory()
                        tracemalloc.stop()

                        return SearchResult(
                            actions = reconstruct_path(child),
                            search_time = end_time - start_time,
                            memory_usage = peak,
                            nodes_expanded = nodes_expanded
                        )
                    frontier.append(child) # add the child to the frontier
                    explored.add(child.state) # add the child state to the explored set 
        end_time = time.perf_counter() # get the end time
        current, peak = tracemalloc.get_traced_memory() # get the current memory usage
        tracemalloc.stop() # stop the memory usage

        return SearchResult( # return the search result
            actions = None,
            search_time = end_time - start_time,
            memory_usage = peak,
            nodes_expanded = nodes_expanded
        )





