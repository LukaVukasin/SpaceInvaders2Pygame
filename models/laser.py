import constants
from models.undamageable_entity import UndamageableEntity


class Laser(UndamageableEntity):

    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            constants.LASER_WIDTH,
            constants.LASER_HEIGHT,
            constants.LASER_IMAGE,
            constants.LASER_SPEED,
        )

    def update(self, dt):
        self.y -= self.speed * dt

    def is_off_screen(self):
        return self.y + self.height < 0
