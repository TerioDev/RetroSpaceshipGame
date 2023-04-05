import pygame

class Settings():
    # This class contains all game settings
    pygame.display.set_caption("Alien invasion")

    def __init__(self):
        # Initialize game settings

        # Screen settings
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (182, 199, 153)

        # Ship settigns
        self.ship_velocity = 1.5