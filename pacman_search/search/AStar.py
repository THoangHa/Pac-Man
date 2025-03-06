# search/AStar.py
"""
AStar search algorithm implementation.
This module contains the AStar class which implements the A* search algorithm
for solving search problems. The A* algorithm uses a priority queue to explore
nodes based on their path cost and heuristic value.
Classes:
    AStar: Implements the A* search algorithm.
Methods:
    search(problem):
        Performs the A* search on the given problem.
        Args:
            problem: An instance of a search problem.
        Returns:
            A SearchResult object containing the actions to reach the goal,
            the search time, memory usage, and the number of nodes expanded.
"""


import time
import tracemalloc
from .Search import SearchAlgorithm, reconstruct_path, SearchResult
from .utils import Node, PriorityQueue

class AStar(SearchAlgorithm):
    """
    A* search algorithm implementation.
    Methods
    -------
    search(problem):
        Executes the A* search algorithm on the given problem.
    search(problem)
        Parameters
        ----------
        problem : Problem
            The problem to be solved by the A* search algorithm.
        Returns
        -------
        SearchResult
            An object containing the result of the search, including the actions to reach the goal,
            the search time, memory usage, and the number of nodes expanded.
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

        frontier = PriorityQueue() # create a priority queue
        frontier.push(root, root.path_cost + problem.heuristic(root.state)) # push the root node to the frontier
        explored = {root.state: root.path_cost} # create a dictionary with the root state

        while not frontier.is_empty(): # while the frontier is not empty
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
                if next_state not in explored or child_cost < explored[next_state]:
                    child = Node(
                        state = next_state,
                        parent = node,
                        action = action,
                        path_cost = child_cost
                    )

                    priority = child_cost + problem.heuristic(next_state)
                    frontier.push(child, priority)
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