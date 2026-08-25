import pygame


class Utils:
    
    @staticmethod
    def aabb(a, b):
        overlaps_x = a.x < b.x + b.width and a.x + a.width > b.x
        overlaps_y = a.y < b.y + b.height and a.y + a.height > b.y

        return overlaps_x and overlaps_y

    @staticmethod
    def load_image(path, width, height):
        image = pygame.image.load(path).convert_alpha()

        return pygame.transform.scale(image, (width, height))
