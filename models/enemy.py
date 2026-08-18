import constants
from models.entity import BaseEntity
from models.enemy_laser import EnemyLaser


class Enemy(BaseEntity):

    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            constants.ENEMY_WIDTH,
            constants.ENEMY_HEIGHT,
            constants.ENEMY_IMAGE,
            constants.ENEMY_SPEED,
        )

    def shoot(self):
        x = self.x + self.width / 2 - constants.ENEMY_LASER_WIDTH / 2
        y = self.y + self.height

        return EnemyLaser(x, y)
