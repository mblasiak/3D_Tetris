from direct.gui.OnscreenText import OnscreenText
from game.Score.ScoreObserver import ScoreObserver
from game.StartClear import StartClear


class ScoreDisplay(ScoreObserver,StartClear):

    def __init__(self, app):
        ScoreObserver.__init__(self)
        font = app.loader.loadFont('resources/fonts/Gobold Uplow Italic.ttf')
        self.app=app
        self.text = OnscreenText(text="", pos=(-0.7, +0.5), scale=0.09, fg=(1, 1, 1, 1))
        self.text.setFont(font)

    def start(self):
        self.text.setText("SCORE: " + str("0"))

    def update(self, score):
        print(score)
        self.text.setText("SCORE: " + str(score))

    def clear(self):
        self.text.setText("")

    def __del__(self):
        self.text.destroy()

