import constants
from models.entity import BaseEntity


class Laser(BaseEntity):

    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            constants.LASER_WIDTH,
            constants.LASER_HEIGHT,
            constants.LASER_IMAGE,
            constants.LASER_SPEED,
        )
