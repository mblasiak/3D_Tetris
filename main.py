from model.Box import Box
from direct.showbase.ShowBase import ShowBase
from model.GameMenager import GameMenager

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        #a=Box(0,20,10,self)
        #a.fall()
        gM=GameMenager(self)
        gM.drop_new()
app = MyApp()
app.run()