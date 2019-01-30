from model.Box import Box
from direct.showbase.ShowBase import ShowBase
from model.GameMenager import GameMenager

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.gM=GameMenager(self)
        self.gM.drop_new()
        self.taskMgr.add(self.gM.movaAll,"MovAll")


app = MyApp()
app.run()