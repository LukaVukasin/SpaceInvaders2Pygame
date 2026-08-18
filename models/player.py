import pygame
import constants
from models.damageable_entity import DamageableEntity
from models.laser import Laser


class Player(DamageableEntity):

    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            constants.PLAYER_WIDTH,
            constants.PLAYER_HEIGHT,
            constants.PLAYER_IMAGES,
            constants.PLAYER_SPEED,
            constants.PLAYER_HP,
            constants.PLAYER_HIT_IMAGE,
        )

        # seconds left before the next shot is allowed
        self.shoot_timer = 0

    def update(self, dt):
        # keeps the hit blink timer running
        super().update(dt)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.speed * dt
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.speed * dt

        self.handle_wall_collision()

        if self.shoot_timer > 0:
            self.shoot_timer -= dt

    def shoot(self):
        self.shoot_timer = constants.PLAYER_SHOOT_COOLDOWN

        x = self.x + self.width / 2 - constants.LASER_WIDTH / 2
        y = self.y - constants.LASER_HEIGHT

        return Laser(x, y)

    def handle_wall_collision(self):
        max_x = constants.SCREEN_WIDTH - self.width

        if self.x <= 0:
            self.x = 0
        elif self.x >= max_x:
            self.x = max_x

    def can_shoot(self):
        return self.shoot_timer <= 0
