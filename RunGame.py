from panda3d.core import loadPrcFileData

from Game import Game

loadPrcFileData('', 'win-size 800 800')
# loadPrcFileData('', 'want-pstats 1')
app = Game()
app.setFrameRateMeter(True)
app.run()
