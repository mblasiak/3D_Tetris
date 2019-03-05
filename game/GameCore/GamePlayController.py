from game.BoxGfx.BoxGfxFactory import BoxGfxFactory
from game.Config import Config
from game.PlayBounds.GameBound import GameBound
from game.GameButtonHandler import GameButtonHandler
from game.GameMap import GameMap
from game.BoxModels.BoxModelFactory import BoxModelFactory
from game.Shapes.ShapesFactory import ShapesFactory

gp = Config.GamePlay
gpm = Config.GamePlay.GameMap
gpfx = Config.GamePlay.Gfx


class GamePlayController:
    def __init__(self, app, score, shapes_factory, map_controller):
        self.current_box = None
        self.mc = map_controller
        self.shapes_factory = shapes_factory
        self.button_handler = GameButtonHandler(app, self.current_box)
        self.score_display = score
        self.bounds = GameBound(app, gpm.X, gpm.Y, gpfx.box_size, gp.Gfx.offset)
        self.wait_counter = 0

    def drop_new(self):
        if not self.mc.check(Config.GamePlay.GameMap.spawn_y, Config.GamePlay.GameMap.spawn_x).is_movable():
            box = self.shapes_factory.get_random()
            self.current_box = box
            self.button_handler.update_box(box)
            self.button_handler.start()
            return True
        return False

    def play(self, task):

        if not self.current_box.is_animation_playing():
            if not self.current_box.fall():
                self.button_handler.stop()
                if self.wait_counter > Config.GamePlay.hold_time:

                    self.wait_counter = 0
                    self.current_box = None
                    self.mc.remove_full_rows()
                    still_playing = self.drop_new()
                    self.score_display.inc()
                    if not still_playing:
                        self.button_handler.stop()
                        return task.done
                else:
                    self.wait_counter += 1
        return task.cont
