class BoxModel:

    def __init__(self, name, model_path):
        self.model_path = model_path
        self.name = name


class WoodenBox(BoxModel):
    def __init__(self):
        super().__init__("wooden","resources/PS2.egg")


class ModelSwitcher:

    def __init__(self):
        self.switcher_dict = {
            1: WoodenBox,
        }

    def number_to_model(self, number):
        if number not in self.switcher_dict:
            return self.switcher_dict[1]
        return self.switcher_dict[number]
