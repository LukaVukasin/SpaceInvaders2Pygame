import constants
from models.damageable_entity import DamageableEntity
from models.enemy_laser import EnemyLaser


class Enemy(DamageableEntity):

    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            constants.ENEMY_WIDTH,
            constants.ENEMY_HEIGHT,
            constants.ENEMY_IMAGES,
            constants.ENEMY_SPEED,
            constants.ENEMY_HP,
            constants.ENEMY_HIT_IMAGE,
        )

    def update(self, dt):
        super().update(dt)

    def shoot(self):
        x = self.x + self.width / 2 - constants.ENEMY_LASER_WIDTH / 2
        y = self.y + self.height

        return EnemyLaser(x, y)
