from game.BoxGfx.BoxGfxFactory import BoxGfxFactory
from game.BoxModels.BoxModelFactory import BoxModelFactory
from game.Config import Config
from game.GameCore.GamePlayController import GamePlayController
from game.GameMap.GameMap import GameMap
from game.Score.Score import Score
from game.ScoreDisplayer.ScoreDisplay import ScoreDisplay
from game.Shapes.ShapesFactory import ShapesFactory

gp = Config.GamePlay
gpm = Config.GamePlay.GameMap
gpfx = Config.GamePlay.Gfx



class MainGame:
    def __init__(self,app):
        self.app=app
        score = Score()
        score.add_observer(ScoreDisplay(app))
        gm = GameMap(gpm.X, gpm.Y)
        gfx_box_factory = BoxGfxFactory(app, BoxModelFactory(app), gpfx.box_size, gpfx.offset, gp.game_speed)
        sf = ShapesFactory(app, gm, gpm.spawn_pos, gfx_box_factory)
        gpc = GamePlayController(app, score, sf, gm)
        gpc.drop_new()
        app.taskMgr.add(gpc.play, "MovAll")







