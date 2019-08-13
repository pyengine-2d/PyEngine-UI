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
        window.set_property("Hauteur", 600)
        window.set_property("Largeur", 900)
        window.set_property("Titre", "PyEngine Game")
        window.set_property("Icon", "")
        window.set_property("FPS Max", 0)
        window.set_property("Update /s", 60)
        window.set_property("Debug", False)
        obj["Window"] = window

        return obj
