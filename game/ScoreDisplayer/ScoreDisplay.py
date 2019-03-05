from direct.gui.OnscreenText import OnscreenText

from game.Score.ScoreObserver import ScoreObserver


class ScoreDisplay(ScoreObserver):

    def __init__(self, app):
        font = app.loader.loadFont('resources/fonts/Gobold Uplow Italic.ttf')
        self.text = OnscreenText(text="SCORE: 0", pos=(-0.7, +0.5), scale=0.09, fg=(1, 1, 1, 1))
        self.text.setFont(font)

    def update(self, score):
        print(score)
        self.text.setText("SCORE: " + str(score))
