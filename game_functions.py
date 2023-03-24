import sys
import pygame

def check_events(ship):
    # React to events triggered by key and mouse inputs

    # Exit the game if quit key is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # If exit key is not pressed check for movement keys
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or pygame.K_d:
                # Move the ship to the right
                ship.moving_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or pygame.K_d:
                ship.moving_right = False

def update_scren(game_class, screen, ship):

    # Background color
    screen.fill(game_class.bg_color)
    
    # Update entities
    ship.blitme()

    # Display modified screen
    pygame.display.flip()