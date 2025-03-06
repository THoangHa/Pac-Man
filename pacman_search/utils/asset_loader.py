# utils/asset_loader.py

"""
This module provides utility functions for loading assets such as images, fonts, and maps for a game.
Functions:
    load_image(image_path, scale_to=None):
        Loads an image from the specified path and optionally scales it to the given dimensions.
        Args:
            image_path (str): The path to the image file.
            scale_to (tuple, optional): The dimensions to scale the image to (width, height). Defaults to None.
        Returns:
            pygame.Surface: The loaded and optionally scaled image, or None if loading fails.
    load_font(font_filename, size, subfolder="Arcade Font"):
        Loads a font from the specified filename and size.
        Args:
            font_filename (str): The name of the font file.
            size (int): The size of the font.
            subfolder (str, optional): The subfolder within the fonts directory where the font file is located. Defaults to "Arcade Font".
        Returns:
            pygame.font.Font: The loaded font, or a default font if loading fails.
    load_map(map_filename):
        Loads a map from a JSON file.
        Args:
            map_filename (str): The name of the map file.
        Returns:
            dict: The loaded map data, or None if loading fails.
"""

import os
import pygame
import json

def load_image(image_path, scale_to = None):

    try:
        image = pygame.image.load(image_path).convert_alpha()
        if scale_to:
            image = pygame.transform.scale(image, scale_to)
        return image

    except Exception as e:
        print(f"Error loading image '{image_path}': {e}")
        return None

def load_font(font_filename, size, subfolder = "Arcade Font"):
    font_path = os.path.join("assets", "fonts", subfolder, font_filename)
    try:
        return pygame.font.Font(font_path, size)
    except Exception as e:
        print(f"Error loading font '{font_path}': {e}")
        return pygame.font.Font(None, size)

def load_map(map_filename):
    map_path = os.path.join("assets", "maps", map_filename)
    try:
        with open(map_path, "r") as map_file:
            return json.load(map_file)
    except Exception as e:
        print(f"Error loading map '{map_path}': {e}")
        return None