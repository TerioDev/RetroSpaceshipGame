import pygame

class Settings():
    # This class contains all game settings
    pygame.display.set_caption("Alien invasion")

    def __init__(self):
        # Initialize game settings

        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (182, 199, 153)