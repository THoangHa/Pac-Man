# search/UCS.py 
"""
Uniform Cost Search (UCS) implementation.
This module contains the UCS class which implements the Uniform Cost Search algorithm
for solving search problems. The UCS algorithm expands the least-cost node first, ensuring
that the path to the goal state is the least costly.
Classes:
    UCS: Inherits from SearchAlgorithm and implements the search method for UCS.
Methods:
    search(problem):
        Performs the UCS algorithm to find the least-cost path to the goal state.
        Args:
            problem: An instance of a search problem that provides the initial state,
                     goal test, and successor function.
        Returns:
            SearchResult: An object containing the actions to reach the goal state,
                          the search time, memory usage, and the number of nodes expanded.
"""


import time
import tracemalloc
from .Search import SearchAlgorithm, reconstruct_path, SearchResult
from .utils import Node, PriorityQueue

class UCS(SearchAlgorithm):
    """
    Uniform Cost Search (UCS) algorithm implementation.
    Methods
    -------
    search(problem)
        Executes the UCS algorithm to find the solution to the given problem.
    """
    """
        Executes the Uniform Cost Search (UCS) algorithm to find the solution to the given problem.
        Parameters
        ----------
        problem : Problem
            The problem to be solved, which must provide methods for getting the initial state, 
            testing the goal state, and getting the successors of a state.
        Returns
        -------
        SearchResult
            An object containing the actions to reach the goal state, the search time, 
            the memory usage, and the number of nodes expanded during the search.
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

        frontier = PriorityQueue()
        frontier.push(root, root.path_cost)
        explored = {root.state: root.path_cost}

        while not frontier.is_empty():
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
                child_cost = node.path_cost + cost
                if next_state not in explored or child_cost < explored[next_state]: # if the child is not in the explored set or the child cost is less than the explored child cost
                    child = Node(
                        state = next_state,
                        parent = node,
                        action = action,
                        path_cost = child_cost
                    )

                    frontier.push(child, child.path_cost)
                    explored[next_state] = child_cost
        
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        return SearchResult(
            actions = None,
            search_time = end_time - start_time,
            memory_usage = peak,
            nodes_expanded = nodes_expanded
        )