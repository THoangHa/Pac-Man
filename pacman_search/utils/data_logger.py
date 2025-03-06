# utils/data_logger.py
"""
DataLogger is a utility class for logging performance metrics of search algorithms.
Attributes:
    log_file (str): The path to the log file where performance data will be stored.
Methods:
    __init__(log_file="logs/performance_log.csv"):
        Initializes the DataLogger instance and creates the log file with headers if it doesn't exist.
    log(algorithm, level, search_time, memory_usage, nodes_expanded, path_length):
        Logs the performance metrics of a search algorithm to the log file.
        Args:
            algorithm (str): The name of the search algorithm.
            level (str): The level or scenario in which the algorithm is executed.
            search_time (float): The time taken by the algorithm to complete the search, in seconds.
            memory_usage (int): The memory usage of the algorithm, in bytes.
            nodes_expanded (int): The number of nodes expanded by the algorithm.
            path_length (int): The length of the path found by the algorithm.
"""



import os
import csv
import datetime

class DataLogger:
    def __init__(self, log_file = "logs\performance_log.csv"):
        self.log_file = log_file

        os.makedirs(os.path.dirname(self.log_file), exist_ok = True)

        if not os.path.exists(self.log_file):
            with open(self.log_file, "w", newline = "") as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Algorithm", "Level", "SearchTimeSec", "MemoryUsageBytes", "NodesExpanded", "PathLength"])

    def log(self, algorithm, level, search_time, memory_usage, nodes_expanded, path_length):
        timestamp = datetime.datetime.now().isoformat()
        with open(self.log_file, "a", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, algorithm, level, search_time, memory_usage, nodes_expanded, path_length])