import pygame
import constants
from models.entity import BaseEntity


class Player(BaseEntity):

    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            constants.PLAYER_WIDTH,
            constants.PLAYER_HEIGHT,
            constants.PLAYER_IMAGE,
            constants.PLAYER_SPEED,
        )

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.speed * dt
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.speed * dt

        self.handle_wall_collision()

    # stops the ship at the left and right edges of the window
    def handle_wall_collision(self):
        max_x = constants.SCREEN_WIDTH - self.width

        if self.x <= 0:
            self.x = 0
        elif self.x >= max_x:
            self.x = max_x
