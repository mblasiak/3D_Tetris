from direct.showbase.ShowBase import ShowBase, ClockObject, AntialiasAttrib
from direct.showbase.ShowBaseGlobal import globalClock

from game.BoxGfx.BoxGfxFactory import BoxGfxFactory
from game.BoxModels.BoxModelFactory import BoxModelFactory
from game.Config import Config
from game.GameCore.GamePlayController import GamePlayController
from game.GameMap import GameMap

from game.Score.Score import Score
from game.ScoreDisplayer.ScoreDisplay import ScoreDisplay
from game.Shapes.ShapesFactory import ShapesFactory

gp = Config.GamePlay
gpm = Config.GamePlay.GameMap
gpfx = Config.GamePlay.Gfx


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.set_up_environment()
        self.set_up_gameplay()

    def set_up_gameplay(self):
        score = Score()
        score.add_observer(ScoreDisplay(self))
        gm = GameMap(gpm.X, gpm.Y)
        gfx_box_factory = BoxGfxFactory(self, BoxModelFactory(self), gpfx.box_size, gpfx.offset, gp.game_speed)
        sf = ShapesFactory(self, gm, gpm.spawn_pos, gfx_box_factory)
        gpc = GamePlayController(self, score, sf, gm)
        gpc.drop_new()
        self.taskMgr.add(gpc.play, "MovAll")

    def set_up_environment(self):
        globalClock.setMode(ClockObject.MLimited)
        globalClock.setFrameRate(120)
        self.render.setAntialias(AntialiasAttrib.MAuto)
        self.disableMouse()
        # self.render.analyze()

