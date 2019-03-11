from direct.gui.DirectButton import DirectButton

from game.StartClear import StartClear


class Menu(StartClear):
    def __init__(self,main_game):
        StartClear.__init__(self)
        self.start_tetris=main_game.start_tetris
        self.menu = []

    def start(self):
        self.menu.append(DirectButton(pos=(0, 0, 0.6), text="Start Game",
                                      scale=.1, pad=(.2, .2), command=self.start_tetris))

        self.menu.append(DirectButton(pos=(0, 0, 0.4), text="Settings",
                                      scale=.1, pad=(.2, .2)))

        self.menu.append(DirectButton(pos=(0, 0, 0.2), text="Scores",
                                      scale=.1, pad=(.2, .2)))

        self.menu.append(DirectButton(pos=(0, 0, -.1), text="Exit",
                                      scale=.1, pad=(.2, .2)))

    def clear(self):
        for button in self.menu:
            button.destroy()
        self.menu.clear()

    def __del__(self):
        self.clear()

