import pygame
from game import Game

# Initialize Pygame and its modules
pygame.init()

# game windows caption
pygame.display.set_caption("Space Invaders")

# creates the game and runs it until the player quits
game = Game()
game.run()

pygame.quit()
