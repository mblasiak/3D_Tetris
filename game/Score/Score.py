from game.Score.ScoreNotifier import ScoreNotifier
from game.StartClear import StartClear


class Score(ScoreNotifier, StartClear):
    def __init__(self):
        ScoreNotifier.__init__(self)
        self.score = 0

    def inc(self):
        self.score += 1
        self.call_observer(self.score)

    def clear(self):
        self.score = 0
        self.call_observer(self.score)

    def start(self):
        self.score = 0
        self.call_observer(self.score)
