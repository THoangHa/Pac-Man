# gui/level_select.py
"""
This module provides the LevelSelect class for displaying a level selection screen in a Pygame application.
Classes:
    LevelSelect: Manages the level selection screen, including displaying buttons for each level and handling user input.
Functions:
    __init__(self, screen): Initializes the LevelSelect instance with the given screen.
    run(self): Runs the level selection loop, handling events and updating the screen.
Attributes:
    screen (pygame.Surface): The Pygame screen surface to draw on.
    clock (pygame.time.Clock): The Pygame clock to control the frame rate.
    running (bool): A flag to control the main loop.
    title_font (pygame.font.Font): The font used for the title text.
    font (pygame.font.Font): The font used for the button text.
    buttons (list): A list of Button objects for each level.
    back_button (Button): A Button object for the "Back" button.
    selected_level (int or None): The currently selected level, or None if no level is selected.
Usage:
    Create an instance of LevelSelect with a Pygame screen surface, then call the run method to display the level selection screen.
"""



import pygame
import sys
from gui.utils import Button, load_font, draw_text
from game.constants import COLOUR_BLACK, COLOUR_WHITE

class LevelSelect:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True

        self.title_font = load_font("EtArtiluxDots-xRR1V.ttf", 72)
        self.font = load_font("EtArtiluxDots-xRR1V.ttf", 36)

        self.buttons = []
        screen_width, screen_height = self.screen.get_size()
        button_width, button_height = 200, 30
        spacing = 10
        total_height = 3 * button_height + 2 * spacing
        start_y = (screen_height - total_height) // 2

        x_center = (screen_width - button_width) // 2
        for i in range(6):
            level_num = i + 1
            button_rect = (
                x_center,
                start_y + i * (button_height + spacing),
                button_width,
                button_height
            )

            btn = Button(
                rect = button_rect,
                text = f"Level {level_num}",
                font = self.font,
                bg_colour = COLOUR_BLACK,
                text_colour = COLOUR_WHITE,
                hover_colour = (200, 200, 200)
            )
            self.buttons.append(btn)

        back_rect = (
            x_center,
            start_y + 6 * (button_height + spacing),
            button_width,
            button_height
        )
        self.back_button = Button(
            rect = back_rect,
            text = "Back",
            font = self.font,
            bg_colour = COLOUR_BLACK,
            text_colour = COLOUR_WHITE,
            hover_colour = (200, 200, 200)
        )

        self.selected_level = None

    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(COLOUR_BLACK)

            draw_text(self.screen, "Select a Level", self.title_font, COLOUR_WHITE, (50, 50))

            for i, btn in enumerate(self.buttons):
                if btn.update(events):
                    self.selected_level = i + 1
                    self.running = False
                btn.draw(self.screen)

            if self.back_button.update(events):
                self.running = False
            self.back_button.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        return self.selected_level

    