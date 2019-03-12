from direct.gui.DirectEntry import DirectEntry
from direct.gui.OnscreenText import OnscreenText

from game.StartClear import StartClear


class GameOver(StartClear):

    def __init__(self):
        StartClear.__init__(self)
        self.sliderText = None
        self.entry = None

    def start(self):
        self.game_text = OnscreenText("GAME OVER", pos=(0, 0.80), scale=.15,
                                       fg=(1, 1, 1, 1), shadow=(0, 0, 0, 1))
        self.entry = DirectEntry(text="", scale=.1, pos=(-0.5, 0.0, 0),
                                 initialText="Type Something", numLines=2, focus=0,focusInCommand=self.clear_name_box)
    def clear_name_box(self):
        self.entry.enterText('')

    def clear(self):
        if self.sliderText is not None:
            self.sliderText.destroy()
        self.sliderText = None
