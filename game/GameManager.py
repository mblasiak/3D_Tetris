import numpy as np
from panda3d.core import DirectionalLight, Fog, AntialiasAttrib

from game.GameBound import GameBound
from game.GameButtonHandler import GameButtonHandler
from game.GameMap import GameMap
from game.BoxModelFactory import BoxModelFactory
from game.Shapes.ScoreDisplay import ScoreDisplay
from game.ShapesFactory import ShapesFactory


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
        app.render.setAntialias(AntialiasAttrib.MAuto)
        app.disableMouse()
        self.app.camera.setPos(0, 40, 10)
        # self.app.camera.setHpr(0, -20,0)
        # # myFog = Fog("Fog")
        # #myFog.setColor(1, 1, 1)
        # myFog.setExpDensity(0.001)
        # app.render.setFog(myFog)

        # dlight = DirectionalLight('my dlight')
        # dlnp = app.render.attachNewNode(dlight)
        # app.render.setLight(dlnp)
        # dlnp.setPos(300,300,0)
        self.bounds = GameBound(app, self)

    def drop_new(self):

        if not self.mc.check(self.top, self.middle).is_movable():
            box = self.shapes_factory.get_random()
            self.current_box = box
            self.app.camera.lookAt(self.current_box.boxes[1].box_gfx.box_holder)

            self.button_handler.update_box(box)
            return True
        return False

    def play(self, task):
        #self.app.camera.lookAt(self.current_box.boxes[1].box_gfx.box_holder)
        self.app.camera.lookAt(self.current_box.get_look_at())

        if not self.current_box.is_animation_playing():
            if not self.current_box.fall():
                self.current_box = None
                self.mc.remove_full_rows()
                still_playing = self.drop_new()
                self.score += 1
                self.score_display.update(self.score)
                if not still_playing:
                    self.button_handler.stop()
                    return task.done
        return task.cont
