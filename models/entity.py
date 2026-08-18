import pygame


class BaseEntity:

    def __init__(self, x, y, width, height, speed):
        # floats, because Rect coordinates are integers and would truncate slow movement
        self.x = float(x)
        self.y = float(y)

        self.width = width
        self.height = height

        # pixels per second
        self.speed = speed

    def get_rect(self):
        return pygame.Rect(round(self.x), round(self.y), self.width, self.height)
