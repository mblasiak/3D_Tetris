from game.Shapes.I_block.IBlock import IBlock
from game.Shapes.J_block.JBlock import JBlock
from game.Shapes.L_block.LBlock import LBlock
from game.Shapes.O_block.OBlock import OBlock
from game.Shapes.S_block.SBlock import SBlock
from game.Shapes.T_block.TBlock import TBlock
from game.Shapes.Z_block.ZBlock import ZBlock


class ShapeSwitcher:

    def __init__(self):
        self.switcher_dict = {
            1: IBlock,
            2: JBlock,
            3: LBlock,
            4: OBlock,
            5: SBlock,
            6: TBlock,
            7: ZBlock

        }

    def number_to_shape(self, number):
        if number not in self.switcher_dict:
            return self.switcher_dict[1]
        return self.switcher_dict[number]
