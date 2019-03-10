from panda3d.core import loadPrcFileData

from game.Game import Game
loadPrcFileData('', 'win-size 800 800')
game = Game()
game.setFrameRateMeter(True)
game.run()
