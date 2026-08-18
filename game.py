import pygame
import constants
from models.player import Player

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode(
            (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT),
            pygame.SCALED,
            vsync=1,
        )

        self.clock = pygame.time.Clock()

        self.running = True

        self.player_lasers = []

        self.player = Player(
            (constants.SCREEN_WIDTH - constants.PLAYER_WIDTH) / 2,
            constants.SCREEN_HEIGHT - constants.PLAYER_HEIGHT - constants.PLAYER_BOTTOM_MARGIN,
        )

    # main game loop
    def run(self):
        while self.running:
            # milliseconds since last frame, capped at MAX_FRAMERATE
            dt_ms = self.clock.tick(constants.MAX_FRAMERATE)
            dt = dt_ms / 1000

            self.handle_events()
            self.update(dt)
            self.draw()

    # reads player input, does not move anything
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # one laser per press, not per frame held
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.player.can_shoot():
                    self.player_lasers.append(self.player.shoot())

    # moves everything, dt is seconds since last frame
    def update(self, dt):
        self.player.update(dt)

        self.update_player_lasers(dt)


    # clears screen, draws back to front, presents the frame
    def draw(self):
        self.screen.fill(constants.COLOR_BLACK)

        self.player.draw(self.screen)

        for laser in self.player_lasers:
            laser.draw(self.screen)

        pygame.display.flip()

    def update_player_lasers(self, dt):
        remaining_lasers = []

        for laser in self.player_lasers:
            laser.update(dt)

            if not laser.is_off_screen():
                remaining_lasers.append(laser)

        self.player_lasers = remaining_lasers

        print("DEBUG player lasers:", len(self.player_lasers))
