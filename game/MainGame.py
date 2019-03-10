from panda3d.core import Camera, PerspectiveLens, NodePath, Lens

from game.BoxGfx.BoxGfxFactory import BoxGfxFactory
from game.BoxModels.BoxModelFactory import BoxModelFactory
from game.Config import Config
from game.GameCore.GamePlayController import GamePlayController
from game.GameMap.GameMap import GameMap
from game.Score.Score import Score
from game.ScoreDisplayer.ScoreDisplay import ScoreDisplay
from game.Shapes.ShapesFactory import ShapesFactory
from game.UpcomingBlockDisplay import UpcomingBlockDisplay

gp = Config.GamePlay
gpm = Config.GamePlay.GameMap
gpfx = Config.GamePlay.Gfx


class MainGame:
    def __init__(self, app):
        self.app = app
        self.score = Score()
        self.score.add_observer(ScoreDisplay(app))
        self.gm = GameMap(gpm.X, gpm.Y)
        model_factory = BoxModelFactory(app)

        self.gfx_box_factory = BoxGfxFactory(app.render, model_factory, gpfx.box_size, gpfx.offset, gp.game_speed)
        self.sf = ShapesFactory(app, self.gm, gpm.spawn_pos, self.gfx_box_factory)
        self.gpc = GamePlayController(self.app, self.score, self.sf, self.gm)

        self.next_block_disp = UpcomingBlockDisplay(app, model_factory)
        lens = PerspectiveLens()
        lens.set_aspect_ratio(0.3 / 1)
        cam = NodePath(Camera("Mycam", lens))

        self.next_block_disp.setCamera(cam)
        self.gpc.add_next_box_type_observer(self.next_block_disp)
        cam.setPos(10, 80, 20)
        self.start()

    def start(self):

        self.app.taskMgr.add(self.game_loop, "game_loop")

    def game_loop(self, task):
        self.gpc.play()
        return task.cont

    def clear(self):
        self.score.reset()
        self.next_block_disp.clear()
        self.gpc.clear()