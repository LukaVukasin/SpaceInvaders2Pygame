SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
MAX_FRAMERATE = 60

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

STAR_COUNT = 80
STAR_MIN_SIZE = 1
STAR_MAX_SIZE = 3
# nearer stars move faster, which gives the field some depth
STAR_MIN_SPEED = 20
STAR_MAX_SPEED = 90

GAME_OVER_TEXT = "GAME OVER"
WIN_TEXT = "YOU WIN"
GAME_OVER_FONT_SIZE = 120

PLAYER_WIDTH = 75
PLAYER_HEIGHT = 75
PLAYER_SPEED = 400
PLAYER_BOTTOM_MARGIN = 40
PLAYER_HP = 3

PLAYER_IMAGES = [
    "images/player-ship.png.png",
    "images/player-ship-damage1.png.png",
    "images/player-ship-damage2.png.png",
]

PLAYER_HIT_IMAGE = "images/player-ship-hit.png.png"

PLAYER_SHOOT_COOLDOWN = 0.5

HIT_BLINK_DURATION = 0.1

LASER_WIDTH = 8
LASER_HEIGHT = 24
LASER_SPEED = 600
LASER_IMAGE = "images/player-laser.png.png"

ENEMY_WIDTH = 72
ENEMY_HEIGHT = 75
ENEMY_SPEED = 0
ENEMY_HP = 2

# one image per hp level, least damaged first
ENEMY_IMAGES = [
    "images/enemy-ship.png.png",
    "images/enemy-ship-damaged.png.png",
]

ENEMY_HIT_IMAGE = "images/enemy-ship-hit.png.png"

ENEMY_HORIZONTAL_SPACING = 20
ENEMY_VERTICAL_SPACING = 20
ENEMY_TOP_MARGIN = 80
ENEMY_LEFT_MARGIN = 120

ENEMY_LASER_WIDTH = 15
ENEMY_LASER_HEIGHT = 15
ENEMY_LASER_SPEED = 400
ENEMY_LASER_IMAGE = "images/enemy-laser.png.png"

ENEMY_SHOOT_INTERVAL = 0.25
