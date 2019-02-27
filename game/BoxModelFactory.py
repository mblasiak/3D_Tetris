class BoxModelFactory:

    def __init__(self, app):
        self.loaded_models = {}
        self.app = app

    def get_model(self, model_type):
        if model_type.name in self.loaded_models.keys():
            return self.loaded_models[model_type.name]
        else:
            box_model = self.app.loader.loadModel("resources/PS2.egg")
            self.loaded_models[model_type.name] = box_model
            return box_model
