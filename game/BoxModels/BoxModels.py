class BoxModel:

    def __init__(self, name, model_path):
        self.model_path = model_path
        self.name = name


class ClassicBox(BoxModel):
    def __init__(self):
        super().__init__("classic", "resources/models/classicBox.egg")


class VeryDarkWoodBox(BoxModel):
    def __init__(self):
        super().__init__("veryDark", "resources/models/woodenVeryDarkBox.egg")


class DarkWoodBox(BoxModel):
    def __init__(self):
        super().__init__("dark", "resources/models/woodenDarkBox.egg")


class SimpleWoodBox(BoxModel):
    def __init__(self):
        super().__init__("simple", "resources/models/woodenSimpleBox.egg")


class CrossBox(BoxModel):
    def __init__(self):
        super().__init__("cross", "resources/models/crossBox.egg")


class FragileBox(BoxModel):
    def __init__(self):
        super().__init__("fragile", "resources/models/fragileBox.egg")

class PinsBox(BoxModel):
    def __init__(self):
        super().__init__("pins", "resources/models/crossPinsBox.egg")



class ModelSwitcher:

    def __init__(self):
        self.switcher_dict = {
            1: ClassicBox,
            2: VeryDarkWoodBox,
            3: DarkWoodBox,
            4: SimpleWoodBox,
            5: CrossBox,
            6: FragileBox,
            7: PinsBox
        }

    def number_to_model(self, number):
        if number not in self.switcher_dict:
            return self.switcher_dict[1]
        return self.switcher_dict[number]
