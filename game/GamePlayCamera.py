from game.GameConfig import GameConfig
from game.SimpleCamera import SimpleCamera


class GamePlayCamera(SimpleCamera):

    def __init__(self, region, renderer,observe):
        super().__init__(region, renderer)
        self.observe=observe

    def reset(self):
        self.setPos(GameConfig.main_camera_start_pos)

    def refresh(self):
        self.lookAt(self.observe)

    def move_with_interval(self):
        super().move_with_interval(GameConfig.main_camera_move_time,GameConfig.main_camera_end_pos)


