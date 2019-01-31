import numpy as np

from .Box import Box


class GameMenager:

    def __init__(self, app):
        self.block_map = np.zeros((20, 10)).tolist()
        self.app = app
        self.all_boxes = []
        self.game_speed = 0.1
        self.box_size = 2
        self.current_box = None

    def check_field(self, y, x):
        if y >= len(self.block_map[:][:]) or y < 0 or x >= len(self.block_map[1]) or x < 0:
            return False
        if self.block_map[y][x] == 0:
            return True
        else:
            return False

    def block_field(self, y, x, box):
        self.block_map[y][x] = box

    def release_field(self, y, x):
        self.block_map[y][x] = 0

    def drop_new(self):
        if self.check_field(19, 5):
            box = Box(self, 5, 19, self.app)
            self.all_boxes.append(box)
            self.current_box = box
            return True
        return False

    def remove_full_row(self):
        for y in self.block_map:
            filled_count = 0
            for x in y:
                if x != 0:
                    filled_count += 1
            print(y)
            if filled_count==len(y):
                for x in range(len(y)):
                    print(x)
                    self.all_boxes.remove(y[x])
                    y[x].remove()
                    y[x]=0

    def moveBlocks(self, task):
        self.app.accept("arrow_left", self.current_box.move_left)
        self.app.accept("arrow_right", self.current_box.move_right)
        if not self.current_box.is_animation_finished():

            if not self.current_box.fall():
                self.remove_full_row()
                still_playing = self.drop_new()
                if not still_playing:
                    return task.done
        return task.cont
