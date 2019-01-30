from panda3d.core import Point3
from direct.interval.IntervalGlobal import Sequence
class Box:


    def __init__(self, game_map, x, y, app):
        self.game_map = game_map
        self.falling = True
        self.x = x
        self.y = y
        self.box = app.loader.loadModel("resources/PS2.egg")
        self.box.reparentTo(app.render)
        self.gfx_x=0
        self.gfx_y=0
        self.gfx_z=50
        self.box.setPos(self.gfx_x, self.gfx_z,self.gfx_y)

    def fall(self):
        self.y = self.y - 1
        pandaPosInterval1 = self.box.posInterval(3,Point3(0, 20, self.gfx_y-10))

        mySequence = Sequence(pandaPosInterval1)

        mySequence.start()
        self.gfx_y = self.gfx_y - 10

    def move_left(self):
        self.x = self.x - 1;

    def move_left(self):
        self.x = self.x + 1;

    def stopFalling(self):
        self.falling = False

    def startFalling(self):
        self.falling = True
