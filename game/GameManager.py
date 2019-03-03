import numpy as np
from panda3d.core import AntialiasAttrib, Point3
from panda3d.fx import FisheyeLens

from game.PlayBounds.GameBound import GameBound
from game.GameButtonHandler import GameButtonHandler
from game.GameMap import GameMap
from game.BoxModels.BoxModelFactory import BoxModelFactory
from game.MainCamera import MainCamera
from game.ScoreDisplayer.ScoreDisplay import ScoreDisplay
from game.Shapes.ShapesFactory import ShapesFactory


class GameManager:

    def __init__(self, app):

        self.SIZE_X = 10
        self.SIZE_Y = 20
        game_space = np.zeros((self.SIZE_Y, self.SIZE_X)).tolist()
        self.mc = GameMap(game_space)
        self.app = app
        self.game_speed = 0.6
        self.box_size = 2
        self.current_box = None
        self.model_factory = BoxModelFactory(app)
        self.top = self.SIZE_Y - 2
        self.middle = round(self.SIZE_X / 2)
        self.shapes_factory = ShapesFactory(self, app, self.mc, self.middle, self.top)
        self.button_handler = GameButtonHandler(app, self.current_box)
        self.score = 0
        self.score_display = ScoreDisplay(app)
        self.cam=MainCamera("Mian",FisheyeLens())
        self.cam.setScene(app.render)
        app.render.setAntialias(AntialiasAttrib.MAuto)
        app.disableMouse()

        self.app.camera.setPos(-20, -50, -20)
        self.move_down_itv = self.app.camera.posInterval(self.game_speed*self.SIZE_Y/2, Point3(-20,70 ,30 ))
        self.move_down_itv.start()
        self.bounds = GameBound(app, self)
        self.wait_counter = 0
        self.wait_count=100

    def drop_new(self):
        # self.app.camera.setPos(-20, 10, 30)
        # self.move_down_itv = self.app.camera.posInterval(self.game_speed * self.SIZE_Y / 2, Point3(-20, 50, -20))
        # self.move_down_itv.start()
        if not self.mc.check(self.top, self.middle).is_movable():
            box = self.shapes_factory.get_random()
            self.current_box = box

            self.button_handler.update_box(box)
            return True
        return False

    def play(self, task):
        # self.app.camera.lookAt(self.current_box.boxes[1].box_gfx.box_holder)
        self.app.camera.lookAt(self.current_box.get_look_at())

        if not self.current_box.is_animation_playing():
            if not self.current_box.fall():
                if self.wait_counter>self.wait_count:
                    self.wait_counter=0
                    self.current_box = None
                    self.mc.remove_full_rows()
                    still_playing = self.drop_new()
                    self.score += 1
                    self.score_display.update(self.score)
                    if not still_playing:
                        self.button_handler.stop()
                        return task.done
                else:
                    self.wait_counter+=1
        return task.cont
