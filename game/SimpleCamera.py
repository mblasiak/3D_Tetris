from panda3d.core import Camera, PerspectiveLens, NodePath, Point3


class SimpleCamera:

    def __init__(self, region, renderer):
        self.cam = Camera("SimpleCamera")
        self.camNp = NodePath(self.cam)
        self.camNp.reparent_to(renderer)
        region.setCamera(self.camNp)

    def setPos(self, x, z, y):
        self.camNp.setPos(x, y, z)

    def setPos(self, pos):
        (x, z, y) = pos
        self.camNp.setPos(x, y, z)

    def lookAt(self, object):
        self.camNp.look_at(object)

    def move_with_interval(self, time, x, y, z):
        self.camNp.posInterval(time, Point3(x, z, y))
        int.start()

    def move_with_interval(self, time, pos):
        (x, z, y) = pos
        int=self.camNp.posInterval(time, Point3(x, z, y))
        int.start()

    def setRegion(self, region):
        region.setCamera(self.camNp)

    def setRender(self, renderer):
        self.camNp.reparent_to(renderer)
