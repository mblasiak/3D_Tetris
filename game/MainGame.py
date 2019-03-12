from panda3d.core import Camera, PerspectiveLens, NodePath, Lens

from game.BoxGfx.BoxGfxFactory import BoxGfxFactory
from game.BoxModels.BoxModelFactory import BoxModelFactory
from game.Config import Config
from game.DB.DBConnector import DBConnector
from game.GameCore.GamePlayController import GamePlayController
from game.GameMap.GameMap import GameMap
from game.GameOverScreen import GameOver
from game.Menu import Menu
from game.Score.Score import Score
from game.ScoreDisplayer.ScoreDisplay import ScoreDisplay
from game.Shapes.ShapesFactory import ShapesFactory
from game.NextBlockDisplay import NextBlockDisplay

gp = Config.GamePlay
gpm = Config.GamePlay.GameMap
gpfx = Config.GamePlay.Gfx


class MainGame:
    def __init__(self, app):
        self.app = app
        self.score = Score()
        self.score_display = ScoreDisplay(app)
        self.score.add_observer(self.score_display)
        self.gm = GameMap(gpm.X, gpm.Y)
        model_factory = BoxModelFactory(app)

        self.gfx_box_factory = BoxGfxFactory(app.render, model_factory, gpfx.box_size, gpfx.offset, gp.game_speed)
        self.sf = ShapesFactory(app, self.gm, gpm.spawn_pos, self.gfx_box_factory)
        self.gpc = GamePlayController(self.app, self.score, self.sf, self.gm)

        self.next_block_disp = NextBlockDisplay(app, model_factory)
        lens = PerspectiveLens()
        lens.set_aspect_ratio(0.3 / 1)
        cam = NodePath(Camera("Mycam", lens))

        self.next_block_disp.setCamera(cam)
        self.gpc.add_next_box_type_observer(self.next_block_disp)
        cam.setPos(10, 80, 20)
        self.menus = Menu(self)
        self.game_over=GameOver()
        self.start()
        self.current_game_state = 0
        self.db_connector=DBConnector()

    def start(self):
        self.app.taskMgr.add(self.game_loop, "game_loop")
        self.menus.start()

    def game_loop(self, task):
        # TODO use type object here
        if self.current_game_state == 1:
            if self.gpc.play() == 0:
                self.clear_tetris()
                self.game_over.start()
                return task.done
        return task.cont


    def clear_tetris(self):
        self.next_block_disp.clear()
        self.gpc.clear()
        self.score_display.clear()

    def start_tetris(self):
        self.menus.clear()
        self.score.start()

        self.score_display.start()
        self.gpc.start()
        self.current_game_state = 1
