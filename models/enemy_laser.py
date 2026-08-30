import constants
from models.undamageable_entity import UndamageableEntity


class EnemyLaser(UndamageableEntity):

    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            constants.ENEMY_LASER_WIDTH,
            constants.ENEMY_LASER_HEIGHT,
            constants.ENEMY_LASER_IMAGE,
            constants.ENEMY_LASER_SPEED,
        )

    def update(self, dt):
        self.y += self.speed * dt

    def is_off_screen(self):
        return self.y > constants.SCREEN_HEIGHT
