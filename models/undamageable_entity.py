from models.entity import BaseEntity
from utils import Utils


class UndamageableEntity(BaseEntity):

    def __init__(self, x, y, width, height, image_path, speed):
        super().__init__(x, y, width, height, speed)

        self.image = Utils.load_image(image_path, width, height)

    def draw(self, surface):
        surface.blit(self.image, self.get_rect())
