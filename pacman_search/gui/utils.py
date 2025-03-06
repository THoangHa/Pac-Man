# gui/utils.py
"""
This module provides utility functions and classes for the Pacman search GUI.
Functions:
    load_font(font_path, size):
        Loads a font from the specified path and size. If loading fails, returns a default system font.
    draw_text(surface, text, font, colour, pos):
        Draws text on a given surface at the specified position with the given font and colour.
Classes:
    Button:
        A class representing a clickable button in the GUI.
        Methods:
            __init__(self, rect, text, font, bg_colour, text_colour, hover_colour=None):
                Initializes the Button with a rectangle, text, font, background colour, text colour, and optional hover colour.
            draw(self, surface):
                Draws the button on the given surface.
            update(self, event_list):
                Updates the button state based on the event list. Returns True if the button is clicked.
"""

import os
import pygame

def load_font(font_path, size):
    font_path = os.path.join("assets", "fonts", "Arcade Font", font_path)
    try:
        return pygame.font.Font(font_path, size)
    except Exception as e:
        print(f"Error loading font: {e}")
        return pygame.font.SysFont(None, size)

def draw_text(surface, text, font, colour, pos):
    text_surface = font.render(text, True, colour)
    surface.blit(text_surface, pos)

class Button:
    def __init__(self, rect, text, font, bg_colour, text_colour, hover_colour = None):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font 
        self.bg_colour = bg_colour
        self.text_colour = text_colour
        self.hover_colour = hover_colour if hover_colour else bg_colour
        self.is_hovered = False

    def update(self, event_list):
        mouse_pos = pygame.mouse.get_pos()
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.is_hovered:
                    return True
        return False

    def draw(self, surface):
        colour = self.hover_colour if self.is_hovered else self.bg_colour
        pygame.draw.rect(surface, colour, self.rect)
        text_surface = self.font.render(self.text, True, self.text_colour)
        text_rect = text_surface.get_rect(center = self.rect.center)
        surface.blit(text_surface, text_rect)






