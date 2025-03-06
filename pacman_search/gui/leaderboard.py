# gui/leaderboard.py 
"""
This module defines the Leaderboard class for displaying a leaderboard screen in a Pygame application.
Classes:
    Leaderboard: A class to manage and display the leaderboard screen.
Functions:
    __init__(self, screen): Initializes the Leaderboard instance with the given screen.
    run(self): Runs the main loop for the leaderboard screen, handling events and rendering.
Attributes:
    screen (pygame.Surface): The Pygame screen surface to draw on.
    clock (pygame.time.Clock): The Pygame clock object to manage frame rate.
    font (pygame.font.Font): The font used for rendering text.
    title_font (pygame.font.Font): The font used for rendering the title text.
    back_button (Button): The button to go back to the previous screen.
    scores (list): A list of tuples containing player names and scores.
Methods:
    __init__(self, screen): Initializes the Leaderboard instance with the given screen.
    run(self): Runs the main loop for the leaderboard screen, handling events and rendering.
"""



import pygame
import sys
from gui.utils import Button, load_font, draw_text
from game.constants import COLOUR_BLACK, COLOUR_WHITE

class Leaderboard:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.font = load_font("EtArtiluxDots-xRR1V.ttf", 36)
        self.title_font = load_font("EtArtiluxDots-xRR1V.ttf", 72)

        screen_width, screen_height = self.screen.get_size()
        button_width, button_height = 200, 50
        spacing = 20
        total_height = 3 * button_height + 2 * spacing
        start_y = (screen_height - total_height) // 2

        self.back_button = Button(
            rect = ((screen_width - button_width) // 2, start_y, button_width, button_height),
            text = "Back",
            font = self.font,
            bg_colour = COLOUR_BLACK,
            text_colour = COLOUR_WHITE,
            hover_colour = (200, 200, 200)
        )

        self.scores = []  # Initialize scores as an empty list

    def run(self):
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(COLOUR_BLACK)
            draw_text(self.screen, "Leaderboard", self.title_font, COLOUR_WHITE, (50, 50))

            start_y = 150
            for i, (name, score) in enumerate(self.scores):
                text = f"{i + 1}. {name} - {score}"
                draw_text(self.screen, text, self.font, COLOUR_WHITE, (100, start_y + i * 40))

            if self.back_button.update(events):
                running = False

            self.back_button.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)