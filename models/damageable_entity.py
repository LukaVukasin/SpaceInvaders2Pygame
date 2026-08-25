import constants
from models.entity import BaseEntity
from helpers.utils import Utils


class DamageableEntity(BaseEntity):

    def __init__(self, x, y, width, height, image_paths, speed, hp, hit_image_path):
        super().__init__(x, y, width, height, speed)

        self.hp = hp

        self.images = []

        for path in image_paths:
            self.images.append(Utils.load_image(path, width, height))

        self.select_image()

        self.hit_image = Utils.load_image(hit_image_path, width, height)

        self.hit_timer = 0

    def update(self, dt):
        if self.hit_timer > 0:
            self.hit_timer -= dt

    def draw(self, surface):
        if self.hit_timer > 0:
            surface.blit(self.hit_image, self.get_rect())
        else:
            surface.blit(self.image, self.get_rect())

    def take_damage(self):
        self.hp -= 1

        self.hit_timer = constants.HIT_BLINK_DURATION

        self.select_image()

    def is_dead(self):
        return self.hp <= 0

    def select_image(self):
        if self.is_dead():
            return

        self.image = self.images[len(self.images) - self.hp]
