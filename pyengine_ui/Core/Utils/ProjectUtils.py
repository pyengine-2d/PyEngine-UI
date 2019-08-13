from pyengine_ui.Core.Utils.ObjectUtils import Object


class Project:
    def __init__(self):
        self.project_name = ""
        self.project_folder = ""
        self.author = "Inconnu"
        self.version = "0.0.1"
        self.objects = self.setup_objects()

    @staticmethod
    def setup_objects():
        obj = {}

        window = Object("Window")
        world = Object("World")
        obj["Window"] = window
        obj["World"] = world

        return obj
