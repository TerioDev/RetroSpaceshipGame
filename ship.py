import pygame

class Ship():

    def __init__(self, game_settings, screen):

        self.screen = screen
        self.game_settings = game_settings

        # Loading an image and getting dimensions
        self.image = pygame.image.load('img/ally_ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Placeme a new ship on the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Center point
        self.center = float(self.rect.centerx)

        # Movement indicator
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Update position

        # Update the center point, not the rectangle
        if self.moving_right:
            self.center += self.game_settings.ship_velocity
        if self.moving_left:
            self.center -= self.game_settings.ship_velocity

        # Update rect object depending on self.center value
        self.rect.centerx = self.center


    def blitme(self):
        # Display a shit in its current position

        self.screen.blit(self.image, self.rect)