# utils/config.py
"""
ConfigManager is a class that handles loading, saving, and managing configuration settings from a JSON file.
Attributes:
    config_file (str): The path to the configuration file.
    config (dict): The dictionary that stores the configuration settings.
Methods:
    __init__(config_file="config.json"):
        Initializes the ConfigManager with the specified configuration file.
    load():
        Loads the configuration from the file if it exists.
    get(key, default=None):
        Retrieves the value for the specified key from the configuration.
        Returns the default value if the key is not found.
    set(key, value):
        Sets the value for the specified key in the configuration and saves it to the file.
    default_config():
        Returns the default configuration settings as a dictionary.
"""



import os
import json

class ConfigManager:
    def __init__(self, config_file = "config.json"):
        self.config_file = config_file
        self.config = {}
        self.load()

    def loaf(self):
        if os.path.exists(self.config_file):
            try:
                with open (self.config_file, "r") as file:
                    self.config = json.load(file)
            except Exception as e:
                print(f"Error saving configuration: {e}")

    def get(self, key, default = None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        self.save()

    def default_config(self):
        return {
            "screen_width": 800,
            "screen_height": 600,
            "fullscreen": False,
        }

