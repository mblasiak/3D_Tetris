import numpy as np

from game.GameField.EmptyField import EmptyField
from game.GameField.OutField import OutField
from game.GameField.TakenField import TakenField


class GameMap:
    def __init__(self,x,y):
        game_space = np.zeros((y, x)).tolist()
        self.blocks_map = game_space

    def check(self, y, x):
        if y >= len(self.blocks_map[:][:]) or y < 0 or x >= len(self.blocks_map[1]) or x < 0:
            return OutField()
        if self.blocks_map[y][x] == 0:
            return EmptyField()
        else:
            return TakenField(self.blocks_map[y][x])

    def block(self, y, x, box):
        self.blocks_map[y][x] = box

    def release(self, y, x, box):
        if self.blocks_map[y][x] == box:
            self.blocks_map[y][x] = 0

    def remove_full_rows(self):
        drop_list = []
        for y in range(len(self.blocks_map)):
            filled_count = 0
            for x in self.blocks_map[y]:
                if x != 0:
                    filled_count += 1
            if filled_count == len(self.blocks_map[y]):
                drop_list.append(y)
                for x in range(len(self.blocks_map[y])):
                    self.blocks_map[y][x].remove()
                    self.blocks_map[y][x] = 0

        if len(drop_list) > 0:
            lowest = min(drop_list)
            for time in range(len(drop_list)):
                for p in range(lowest, len(self.blocks_map)):
                    for j in self.blocks_map[p]:
                        if j != 0:
                            j.fall()

    def clear(self):
        for y in range(len(self.blocks_map)):
            for x in range(len(self.blocks_map[y])):
                if self.blocks_map[y][x] != 0:
                    self.blocks_map[y][x].remove()
                    self.blocks_map[y][x] = 0

    def __del__(self):
        self.clear()