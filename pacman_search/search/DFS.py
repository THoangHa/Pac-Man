# search/DFS.py
"""
Depth-First Search (DFS) algorithm implementation.
This module contains the DFS class, which inherits from the SearchAlgorithm class and implements the depth-first search algorithm for solving search problems.
Classes:
    DFS: Implements the depth-first search algorithm.
Methods:
    search(problem):
        Performs a depth-first search on the given problem.
        Args:
            problem: An instance of a search problem.
        Returns:
            A SearchResult object containing the actions to reach the goal, the search time, memory usage, and the number of nodes expanded.
"""
import time
import tracemalloc
from .Search import SearchAlgorithm, reconstruct_path, SearchResult
from .utils import Node

class DFS(SearchAlgorithm):
    """
    Depth-First Search (DFS) algorithm implementation.
    Methods
    -------
    search(problem):
        Executes the DFS algorithm to find a solution to the given problem.
    """
    """
        Perform a depth-first search on the given problem.
        Parameters
        ----------
        problem : Problem
            The problem to be solved, which must provide methods for getting the initial state,
            testing the goal state, and getting successors of a state.
        Returns
        -------
        SearchResult
            An object containing the actions to reach the goal, the search time, memory usage,
            and the number of nodes expanded during the search.
    """

    def search(self, problem):
        start_time = time.perf_counter()
        tracemalloc.start()
        nodes_expanded = 0

        initial_state = problem.get_initial_state()
        # Create the root node
        root = Node(state = initial_state, parent = None, action = None, path_cost = 0)

        if problem.goal_test(root.state): # if the root is the goal state
            end_time = time.perf_counter()
            current, peak  = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            return SearchResult(
                actions = reconstruct_path(root),
                search_time = end_time - start_time,
                memory_usage = peak,
                nodes_expanded = nodes_expanded
            )

        frontier = [root]
        explored = set([root.state])

        while frontier: # while the frontier is not empty
            node = frontier.pop()
            nodes_expanded += 1

            if problem.goal_test(node.state): # if the node is the goal state
                end_time = time.perf_counter()
                current, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                return SearchResult(
                    actions = reconstruct_path(node),
                    search_time = end_time - start_time,
                    memory_usage = peak,
                    nodes_expanded = nodes_expanded
                )
            for action, next_state, cost in problem.get_successors(node.state): # get the successors of the node
                if next_state not in explored:
                    child = Node(
                        state = next_state,
                        parent = node,
                        action = action,
                        path_cost = node.path_cost + cost
                    )

                    frontier.append(child)
                    explored.add(child.state)

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        return SearchResult(
            actions = None,
            search_time = end_time - start_time,
            memory_usage = peak,
            nodes_expanded = nodes_expanded
        )

          