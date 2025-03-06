# main.py

import pygame
import os
from gui.menu import Menu

def resource_path(relative_path):
    """
    Get the absolute path to the resource, works for dev and PyInstaller.
    When using PyInstaller with --onefile, sys._MEIPASS is where bundled files are unpacked.
    """
    try:
        base_path = sys._MEIPASS  # type: ignore[attr-defined]
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def main():

    pygame.init()
    
    screen_width = 800
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pac-Man Search Game")

    menu = Menu(screen)
    menu.run()

if __name__ == "__main__":
    main()