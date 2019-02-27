class Direction:
    def __init__(self, x, y):
        self.y = y
        self.x = x


class OneUp(Direction):
    def __init__(self):
        super().__init__(0, 1)


class OneDown(Direction):
    def __init__(self):
        super().__init__(0, -1)


class OneLeft(Direction):
    def __init__(self):
        super().__init__(-1, 0)


class OneRight(Direction):
    def __init__(self):
        super().__init__(1, 0)
