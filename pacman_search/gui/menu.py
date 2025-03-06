# gui/menu.py
"""
This module defines the Menu class for the Pac-Man game.
Classes:
    Menu: Represents the main menu of the game with options to start the game, view the leaderboard, and exit.
Functions:
    __init__(self, screen): Initializes the Menu with buttons and fonts.
    run(self): Runs the main loop of the menu, handling events and drawing buttons.
    start_game(self): Starts the game by transitioning to the game screen.
    show_leaderboard(self): Displays the leaderboard screen.
"""


import pygame
import sys
from gui.utils import Button, load_font, draw_text
from game.constants import COLOUR_BLACK, COLOUR_WHITE
from gui.game_screen import GameScreen
from gui.leaderboard import Leaderboard
from gui.level_select import LevelSelect

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = load_font("EtArtiluxDots-xRR1V.ttf", 36)
        self.title_font = load_font("EtArtiluxDots-xRR1V.ttf", 72)

        screen_width, screen_height = self.screen.get_size()
        button_width, button_height = 200, 50
        spacing = 20
        total_height = 3 * button_height + 2 * spacing
        start_y = (screen_height - total_height) // 2

        self.start_button = Button(
            rect = ((screen_width - button_width) // 2, start_y, button_width, button_height),
            text = "Start Game",
            font = self.font,
            bg_colour = COLOUR_BLACK,
            text_colour = COLOUR_WHITE,
            hover_colour = (200, 200, 200)
        )

        self.leaderboard_button = Button(
            rect = ((screen_width - button_width) // 2, start_y + button_height + spacing, button_width, button_height),
            text = "Leaderboard",
            font = self.font,
            bg_colour = COLOUR_BLACK,
            text_colour = COLOUR_WHITE,
            hover_colour = (200, 200, 200)
        )

        self.exit_button = Button(
            rect = ((screen_width - button_width) // 2, start_y + 2 * (button_height + spacing), button_width, button_height),
            text = "Exit",
            font = self.font,
            bg_colour = COLOUR_BLACK,
            text_colour = COLOUR_WHITE,
            hover_colour = (200, 200, 200)
        )

    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(COLOUR_BLACK)
            draw_text(self.screen, "PAC-MAN", self.title_font, COLOUR_WHITE, (100, 50))

            if self.start_button.update(events):
                self.start_game()
            if self.leaderboard_button.update(events):
                self.show_leaderboard()
            if self.exit_button.update(events):
                pygame.quit()
                sys.exit()

            self.start_button.draw(self.screen)
            self.leaderboard_button.draw(self.screen)
            self.exit_button.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

    def start_game(self):
        level_select = LevelSelect(self.screen)
        chosen_level = level_select.run()

        if chosen_level is not None:
            game = GameScreen(self.screen, level = chosen_level)
            game.run()

    def show_leaderboard(self):
        leaderboard = Leaderboard(self.screen)
        leaderboard.run()
