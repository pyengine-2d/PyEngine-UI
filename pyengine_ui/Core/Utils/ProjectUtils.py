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

        window = Object("Fenetre", "Window")
        world = Object("Monde", "World")
        world.parent = window
        window.childs["Monde"] = world

        obj["Fenetre"] = window

        return obj
