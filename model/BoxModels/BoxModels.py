class BoxModel:

    def __init__(self, name, model_path):
        self.model_path = model_path
        self.name = name


class WoodenBox(BoxModel):
    def __init__(self):
        super().__init__("wooden","resources/PS2.egg")
