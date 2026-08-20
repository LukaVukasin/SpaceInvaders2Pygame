import constants
from models.enemy import Enemy


class LevelLoader:

    @staticmethod
    def load_tile_map(tilemap):
        enemies = []

        for row_index in range(len(tilemap)):
            row = tilemap[row_index]

            for column_index in range(len(row)):
                tile = row[column_index]

                if tile == 1:
                    x = column_index * (constants.ENEMY_WIDTH + constants.ENEMY_HORIZONTAL_SPACING) + constants.ENEMY_LEFT_MARGIN
                    y = row_index * (constants.ENEMY_HEIGHT + constants.ENEMY_VERTICAL_SPACING) + constants.ENEMY_TOP_MARGIN

                    enemies.append(Enemy(x, y))

        return enemies