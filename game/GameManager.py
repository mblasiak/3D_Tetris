from game.BoxGfx.BoxGfxFactory import BoxGfxFactory
from game.Config import Config
from game.PlayBounds.GameBound import GameBound
from game.GameButtonHandler import GameButtonHandler
from game.GameMap import GameMap
from game.BoxModels.BoxModelFactory import BoxModelFactory
from game.ScoreDisplayer.ScoreDisplay import ScoreDisplay
from game.Shapes.ShapesFactory import ShapesFactory


class GameManager:

    def __init__(self, app):

        self.SIZE_X = 10
        self.SIZE_Y = 20
        self.mc = GameMap()
        self.app = app
        self.game_speed = 0.6
        # self.box_size = 2
        self.current_box = None
        self.model_factory = BoxModelFactory(app)
        self.gfx_box_factoy = BoxGfxFactory(app,self.model_factory, Config.GamePlay.Gfx.box_size,
                                            Config.GamePlay.Gfx.offset, Config.GamePlay.game_speed)
        self.shapes_factory = ShapesFactory(self, app, self.mc, Config.GamePlay.GameMap.spawn_x,
                                            Config.GamePlay.GameMap.spawn_y, self.gfx_box_factoy,Config.GamePlay.Gfx.box_size)
        self.button_handler = GameButtonHandler(app, self.current_box)
        self.score_display = ScoreDisplay(app)
        self.bounds = GameBound(app, self, Config.GamePlay.Gfx)

        ####################################
        # self.app.camera.setPos(-20, -50, -20)
        # self.move_down_itv = self.app.camera.posInterval(self.game_speed * self.SIZE_Y / 2, Point3(-20, 70, 30))
        # self.move_down_itv.start()

        self.wait_counter = 0

    def drop_new(self):
        if not self.mc.check(Config.GamePlay.GameMap.spawn_y, Config.GamePlay.GameMap.spawn_x).is_movable():
            box = self.shapes_factory.get_random()
            self.current_box = box

            self.button_handler.update_box(box)
            return True
        return False

    def play(self, task):
        # self.app.camera.lookAt(self.current_box.get_look_at())

        if not self.current_box.is_animation_playing():
            if not self.current_box.fall():
                if self.wait_counter > Config.GamePlay.hold_time:
                    self.wait_counter = 0
                    self.current_box = None
                    self.mc.remove_full_rows()
                    still_playing = self.drop_new()
                    self.score_display.add_point()
                    if not still_playing:
                        self.button_handler.stop()
                        return task.done
                else:
                    self.wait_counter += 1
        return task.cont
