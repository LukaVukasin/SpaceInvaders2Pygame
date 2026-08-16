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

    # moves everything, dt is seconds since last frame
    def update(self, dt):
        self.player.update(dt)

    # clears screen, draws back to front, presents the frame
    def draw(self):
        self.screen.fill(constants.COLOR_BLACK)

        self.player.draw(self.screen)

        pygame.display.flip()
