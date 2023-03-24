import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

    # Init game and create screen object
    pygame.init()

    # From settings
    game_class = Settings()
    screen = pygame.display.set_mode((game_class.screen_width, game_class.screen_height))

    # Entities
    ship = Ship(screen)

    # Main game loop
    while True:

        gf.check_events(ship)
        ship.update()
        gf.update_scren(game_class, screen, ship)

run_game()