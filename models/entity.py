import pygame


class BaseEntity:

    def __init__(self, x, y, width, height, image_path, speed):
        # floats, because Rect coordinates are integers and would truncate slow movement
        self.x = float(x)
        self.y = float(y)

        self.width = width
        self.height = height

        # pixels per second
        self.speed = speed

        image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(image, (width, height))

    def get_rect(self):
        return pygame.Rect(round(self.x), round(self.y), self.width, self.height)

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.get_rect())
