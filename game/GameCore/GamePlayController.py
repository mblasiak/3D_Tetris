from game.Config import Config
from game.GameCore.CurrentBoxNotifier import CurrentBoxNotifier
from game.GameCore.NextBoxNotifier import NextBoxNotifier
from game.PlayBounds.GameBound import GameBound
from game.GameButtonHandler import GameButtonHandler

gp = Config.GamePlay
gpm = Config.GamePlay.GameMap
gpfx = Config.GamePlay.Gfx


class GamePlayController(CurrentBoxNotifier, NextBoxNotifier):
    def __init__(self, app, score, shapes_factory, map_controller):
        CurrentBoxNotifier.__init__(self)
        NextBoxNotifier.__init__(self)
        self.current_box = None
        self.mc = map_controller
        self.shapes_factory = shapes_factory
        self.button_handler = GameButtonHandler(app, self.current_box)
        self.score_display = score
        self.bounds = GameBound(app, gpm.X, gpm.Y, gpfx.box_size, gp.Gfx.offset)
        self.wait_counter = 0

        self.nex_box_type = self.shapes_factory.get_random_type()
        self.call_next_box_type_observers(self.nex_box_type)

        self.drop_new()

    def drop_new(self):
        if not self.mc.check(Config.GamePlay.GameMap.spawn_y, Config.GamePlay.GameMap.spawn_x).is_movable():
            box = self.shapes_factory.get_shape_from_numb(self.nex_box_type)
            self.current_box = box
            self.call_box_observers(self.current_box)
            self.button_handler.update_box(box)
            self.button_handler.start()
            self.nex_box_type = self.shapes_factory.get_random_type()
            self.call_next_box_type_observers(self.nex_box_type)
            return True
        return False

    def clear(self):
        self.button_handler.stop()
        self.mc.clear()

    def play(self):

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
                        self.mc.clear()
                else:
                    self.wait_counter += 1
