import pygame
from game import Game

pygame.init()

pygame.display.set_caption("Space Invaders")

game = Game()
game.run()

pygame.quit()
