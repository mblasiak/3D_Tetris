class Config:
    class GamePlayCamera:
        start_pos = (-20, -50, -20)
        end_pos = (-20, 70, 30)
        move_time = 5

    class NextBlockRegion:
        cords = (0, 1, 0.8, 1)
        sort = 20

    class GamePlay:
        game_speed = 0.6

        hold_time = 100

        class GameMap:
            X = 10
            Y = 20
            spawn_y = Y - 2
            spawn_x = round(X / 2)

        class Gfx:
            box_size = 2
            offset=(-30,-20,100)

