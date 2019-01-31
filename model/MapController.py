class MapController:
    def __init__(self, block_map):
        self.blocks_map = block_map

    def check_field(self, y, x):
        if y >= len(self.blocks_map[:][:]) or y < 0 or x >= len(self.blocks_map[1]) or x < 0:
            return False
        if self.blocks_map[y][x] == 0:
            return True
        else:
            return False

    def block_field(self, y, x, box):
        self.blocks_map[y][x] = box

    def release_field(self, y, x):
        self.blocks_map[y][x] = 0

    def remove_full_row(self):

        for y in self.blocks_map:
            filled_count = 0
            for x in y:
                if x != 0:
                    filled_count += 1
            if filled_count == len(y):
                for x in range(len(y)):
                    y[x].remove()
                    y[x] = 0

        for y in self.blocks_map:
            for x in y:
                if x != 0:
                    x.fall()
