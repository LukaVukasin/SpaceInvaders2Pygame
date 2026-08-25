import random

import pygame
import constants
from models.entity import BaseEntity


class Star(BaseEntity):

    def __init__(self):
        x = random.uniform(0, constants.SCREEN_WIDTH)
        y = random.uniform(0, constants.SCREEN_HEIGHT)

        size = random.randint(constants.STAR_MIN_SIZE, constants.STAR_MAX_SIZE)
        speed = random.uniform(constants.STAR_MIN_SPEED, constants.STAR_MAX_SPEED)

        super().__init__(x, y, size, size, speed)

    def update(self, dt):
        self.y += self.speed * dt

        if self.y > constants.SCREEN_HEIGHT:
            self.y = -self.height
            self.x = random.uniform(0, constants.SCREEN_WIDTH)

    def draw(self, surface):
        pygame.draw.rect(surface, constants.COLOR_WHITE, self.get_rect())
