import random
import pygame
from const import *

class Board :

    def __init__(self):
        self.mine_field = [
            [None for _ in range(9)] for _ in range(9)
        ]

        max_mine_count = 10
        mine_count = 0

        def calculate_mine_count(x, y):
            result = 0

            for y_delta in [-1, 0, 1]:
                for x_delta in [-1, 0, 1]:
                    try:
                        value = self.mine_field[y + y_delta][x + x_delta]
                        if value == FIELD_MINE:
                            result += 1
                    except IndexError:
                        pass
            return result


        # None이라면 FILED_MINE 대입
        while mine_count < max_mine_count:
            x = random.randrange(0, 9)
            y = random.randrange(0, 9)
            if self.mine_field[y][x] is None:
                self.mine_field[y][x] = FIELD_MINE
                mine_count += 1

        # 해당 칸을 기준으로 주변 8칸에 지뢰가 몇개 있는지 나타냄
        for y in range(9):
            for x in range(9):
                if self.mine_field[y][x] is None:
                    mine_count = calculate_mine_count(x, y)
                    self.mine_field[y][x] = mine_count

        print(self.mine_field)


    def draw(self, surface):
        start_x = SCREEN_WIDTH / 2 - (26 * 9) / 2
        start_y = SCREEN_HEIGHT / 2 - (26 * 9) / 2

        size = int(SCREEN_HEIGHT / 9)

        for y in range(9):
            for x in range(9):
                rect = (start_x + x * size, start_y + y * size, size + 1, size + 1)
                pygame.draw.rect(surface, WHITE, rect, 1)
                value = self.mine_field[y][x]
                if value == FIELD_MINE:
                    pygame.draw.rect(surface, WHITE, rect, 10)
                else:
                    pygame.draw.rect(surface, (255, 255, 0), rect, value)

    def on_click(self, pos, button):
        print(f"pos: {pos}, button: {button}")
        start_x = SCREEN_WIDTH / 2 - (26 * 9) / 2
        start_y = SCREEN_HEIGHT / 2 - (26 * 9) / 2
        size = int(SCREEN_HEIGHT / 9)
        relative_pos = (pos[0] - start_x, pos[1] - start_y)

        if relative_pos[0] < 0: return
        if relative_pos[1] < 0: return

        if size * 9 < relative_pos[0]: return
        if size * 9 < relative_pos[1]: return

        index_pos = (int(relative_pos[0] / size), int(relative_pos[1] / size))
        print(f"index_pos: {index_pos}")