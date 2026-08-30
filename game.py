import random
import pygame
import constants
from models.player import Player
from models.star import Star
from helpers.level_loader import LevelLoader
from helpers.levels import LEVEL_1, LEVEL_2
from helpers.utils import Utils

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(
            (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT),
            pygame.SCALED,
            vsync=1,
        )

        self.clock = pygame.time.Clock()

        self.running = True

        self.stars = []

        for _ in range(constants.STAR_COUNT):
            self.stars.append(Star())

        self.player_lasers = []

        self.game_finished = False

        self.game_over = False

        self.game_won = False

        self.font = pygame.font.Font(None, constants.GAME_OVER_FONT_SIZE)

        self.enemy_lasers = []

        self.enemies = LevelLoader.load_tile_map(LEVEL_2)

        self.enemy_shoot_timer = self.get_enemy_shoot_interval()

        self.player = Player(
            (constants.SCREEN_WIDTH - constants.PLAYER_WIDTH) / 2,
            constants.SCREEN_HEIGHT - constants.PLAYER_HEIGHT - constants.PLAYER_BOTTOM_MARGIN,
        )

    # main game loop
    def run(self):
        while self.running:
            dt_ms = self.clock.tick(constants.MAX_FRAMERATE)
            dt = dt_ms / 1000

            self.handle_events()
            self.update(dt)
            self.draw()
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif not self.game_finished:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.player.can_shoot():
                        self.player_lasers.append(self.player.shoot())
    def update(self, dt):
        if not self.game_finished:
            self.player.update(dt)

        self.update_stars(dt)

        self.update_enemies(dt)

        self.update_player_lasers(dt)

        self.handle_laser_hits()

        self.update_enemy_shooting(dt)

        self.update_enemy_lasers(dt)

        self.handle_player_hits()

        self.check_win()

    def draw(self):
        self.screen.fill(constants.COLOR_BLACK)

        for star in self.stars:
            star.draw(self.screen)

        for enemy in self.enemies:
            enemy.draw(self.screen)

        if not self.game_finished:
            self.player.draw(self.screen)

        for laser in self.player_lasers:
            laser.draw(self.screen)

        for laser in self.enemy_lasers:
            laser.draw(self.screen)

        if self.game_finished:
            self.draw_game_finished()

        pygame.display.flip()

    def draw_game_finished(self):
        if self.game_won:
            message = constants.WIN_TEXT
        else:
            message = constants.GAME_OVER_TEXT

        text = self.font.render(message, True, constants.COLOR_WHITE)

        x = (constants.SCREEN_WIDTH - text.get_width()) / 2
        y = (constants.SCREEN_HEIGHT - text.get_height()) / 2

        self.screen.blit(text, (x, y))

    def check_win(self):
        if not self.enemies:
            self.game_won = True

            self.game_finished = True
    def update_stars(self, dt):
        for star in self.stars:
            star.update(dt)

    # enemies do not move, but they still need their hit blink timer to run
    def update_enemies(self, dt):
        for enemy in self.enemies:
            enemy.update(dt)

    def update_player_lasers(self, dt):
        remaining_lasers = []

        for laser in self.player_lasers:
            laser.update(dt)

            if not laser.is_off_screen():
                remaining_lasers.append(laser)

        self.player_lasers = remaining_lasers

        print("DEBUG player lasers:", len(self.player_lasers))

    def update_enemy_lasers(self, dt):
        remaining_lasers = []

        for laser in self.enemy_lasers:
            laser.update(dt)

            if not laser.is_off_screen():
                remaining_lasers.append(laser)

        self.enemy_lasers = remaining_lasers

        print("DEBUG enemy lasers:", len(self.enemy_lasers))

    # one shot per interval for the whole fleet, fired by a random enemy
    def update_enemy_shooting(self, dt):
        if not self.enemies:
            return

        self.enemy_shoot_timer -= dt

        if self.enemy_shoot_timer <= 0:
            shooter = random.choice(self.enemies)

            new_enemy_laser = shooter.shoot()

            self.enemy_lasers.append(new_enemy_laser)

            self.enemy_shoot_timer = self.get_enemy_shoot_interval()

    # fewer enemies left means a longer wait between shots
    def get_enemy_shoot_interval(self):
        return constants.ENEMY_SHOOT_INTERVAL_PER_ENEMY / len(self.enemies)

    def handle_player_hits(self):
        remaining_lasers = []

        for laser in self.enemy_lasers:
            if Utils.aabb(laser, self.player):
                self.player.take_damage()

                if self.player.is_dead():
                    self.game_over = True

                    self.game_finished = True
            else:
                remaining_lasers.append(laser)

        self.enemy_lasers = remaining_lasers

    def handle_laser_hits(self):
        remaining_lasers = []

        for laser in self.player_lasers:
            hit_enemy = None

            for enemy in self.enemies:
                if Utils.aabb(laser, enemy):
                    hit_enemy = enemy
                    break

            if hit_enemy is None:
                remaining_lasers.append(laser)
            else:
                hit_enemy.take_damage()

                if hit_enemy.is_dead():
                    self.enemies.remove(hit_enemy)

        self.player_lasers = remaining_lasers
