# search/utils.py
"""
This module provides utility classes and functions for search algorithms.
Classes:
    Node: Represents a node in a search tree.
    PriorityQueue: Implements a priority queue using a heap.
Functions:
    null_heuristic(state): A heuristic function that always returns 0.
Class Node:
    __init__(self, state, parent=None, action=None, path_cost=0):
        Initializes a new node.
        Args:
            state: The state represented by the node.
            parent: The parent node.
            action: The action taken to reach this node.
            path_cost: The cost to reach this node.
    __lt__(self, other):
        Compares this node with another node based on path cost.
        Args:
            other: The other node to compare with.
        Returns:
            True if this node's path cost is less than the other node's path cost.
    __repr__(self):
        Returns a string representation of the node.
Class PriorityQueue:
    __init__(self):
        Initializes a new priority queue.
    push(self, item, priority):
        Adds an item to the priority queue with the given priority.
        Args:
            item: The item to add.
            priority: The priority of the item.
    pop(self):
        Removes and returns the item with the highest priority (lowest priority value).
        Returns:
            The item with the highest priority.
    is_empty(self):
        Checks if the priority queue is empty.
        Returns:
            True if the priority queue is empty, False otherwise.
Function null_heuristic(state):
    A heuristic function that always returns 0.
    Args:
        state: The state for which the heuristic value is calculated.
    Returns:
        0
"""



import heapq

class Node: 
    """
    A class used to represent a Node in a search tree.
    Attributes
    ----------
    state : any
        The state represented by the node.
    parent : Node, optional
        The parent node of this node (default is None).
    action : any, optional
        The action taken to get to this node from the parent node (default is None).
    path_cost : int, optional
        The cost to reach this node from the root node (default is 0).
    Methods
    -------
    __lt__(other)
        Compares this node with another node based on path_cost.
    __repr__()
        Returns a string representation of the node.
    """

    def __init__(self, state, parent = None, action = None, path_cost = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        
    def __lt__(self, other):
        return self.path_cost < other.path_cost

    def __repr__(self):
        return f"Node(state = {self.state}, path_cost = {self.path_cost})"

class PriorityQueue:
    """
    A priority queue implementation using a heap.
    Attributes:
        elements (list): A list to store the elements of the priority queue.
        count (int): A counter to maintain the order of elements with the same priority.
    Methods:
        __init__():
            Initializes an empty priority queue.
        push(item, priority):
            Adds an item to the priority queue with the given priority.
        pop():
            Removes and returns the item with the highest priority (lowest priority number).
        is_empty():
            Checks if the priority queue is empty.
    """

    def __init__(self):
        self.elements = []
        self.count = 0

    def push(self, item, priority):
        heapq.heappush(self.elements, (priority, self.count, item))
        self.count += 1

    def pop(self):
        return heapq.heappop(self.elements)[2]

    def is_empty(self):
        return len(self.elements) == 0


def null_heuristic(state): 
    """
    A heuristic function that always returns zero.
    This heuristic is used in search algorithms where no heuristic information is available or needed.
    Args:
        state: The current state of the search problem.
    Returns:
        int: Always returns 0.
    """

    return 0