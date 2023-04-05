import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

    # Init game and create screen object
    pygame.init()

    # From settings
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))

    # Entities
    ship = Ship(game_settings, screen)

    # Main game loop
    while True:

        gf.check_events(ship)
        ship.update()
        gf.update_scren(game_settings, screen, ship)

run_game()