import numpy as np

from .Box import Box


class GameMenager:

    def __init__(self, app):
        self.block_map = np.zeros((20, 10)).tolist()
        self.app = app
        self.all_boxes = []
        self.game_speed = 0.1
        self.current_box=None

    def check_field(self, y, x):
        if y >= len(self.block_map[:][:]) or y < 0 or x >= len(self.block_map[1]) or x < 0:
            return False
        if self.block_map[y][x] == 0:
            return True
        else:
            return False

    def block_field(self, y, x):
        self.block_map[y][x] = 1

    def release_field(self, y, x):
        self.block_map[y][x] = 0

    def drop_new(self):
        print("WAna Drop")
        if self.check_field(19, 9):
            box = Box(self, 9, 19, self.app)
            self.all_boxes.append(box)
            self.current_box=box
            print("New")
            print(len(self.all_boxes))

    def moveBlocks(self, task):

        if not self.current_box.is_animation_finished():
            print("STOPED PLAYING")
            if not self.current_box.fall():
                self.drop_new()
        return task.cont
