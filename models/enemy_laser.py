import constants
from models.entity import BaseEntity


class EnemyLaser(BaseEntity):

    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            constants.ENEMY_LASER_WIDTH,
            constants.ENEMY_LASER_HEIGHT,
            constants.ENEMY_LASER_IMAGE,
            constants.ENEMY_LASER_SPEED,
        )

    # positive, because this one travels down the screen
    def update(self, dt):
        self.y += self.speed * dt

    def is_off_screen(self):
        return self.y > constants.SCREEN_HEIGHT
