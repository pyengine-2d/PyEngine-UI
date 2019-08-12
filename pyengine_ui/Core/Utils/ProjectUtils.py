from pyengine_ui.Core.Utils.PropertiesUtils import Object


class Project:
    def __init__(self):
        self.project_name = ""
        self.project_folder = ""
        self.objects = self.setup_objects()

    @staticmethod
    def setup_objects():
        obj = {}

        window = Object("Window")
        window.set_properties("height", 600)
        window.set_properties("width", 900)
        window.set_properties("title", "PyEngine Game")
        window.set_properties("debug", False)
        obj["Window"] = window

        return obj
