import pygame

class Ship():

    def __init__(self, screen):

        self.screen = screen

        # Loading an image and getting dimensions
        self.image = pygame.image.load('img/ally_ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Placeme a new ship on the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement indicator
        self.moving_right = False

    def update(self):
        # Update position

        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        # Display a shit in its current position

        self.screen.blit(self.image, self.rect)