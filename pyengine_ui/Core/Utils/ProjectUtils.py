from pyengine_ui.Core.Utils.ObjectUtils import Object

import json
import os


class Project:
    def __init__(self):
        self.project_name = ""
        self.project_folder = ""
        self.author = "Inconnu"
        self.version = "0.0.1"
        self.objects = self.setup_objects()

    def all_objects(self, element=None):
        if element is None:
            elements = self.objects
        else:
            elements = element.childs
        if len(elements):
            obj = elements
            for v in elements.values():
                obj = {**obj, **self.all_objects(v)}
        else:
            obj = {}
        return obj

    def save(self):
        objects = {k: v.to_json() for k, v in self.objects.items()}
        file = {"Name": self.project_name, "Folder": self.project_folder, "Author": self.author,
                "Version": self.version, "Objects": objects}
        with open(os.path.join(self.project_folder, self.project_name, "project.json"), "w") as f:
            f.write(json.dumps(file, indent=4))

    def load(self, file):
        with open(file, "r") as f:
            dic = json.load(f)
        self.project_name = dic["Name"]
        self.project_folder = dic["Folder"]
        self.author = dic["Author"]
        self.version = dic["Version"]
        self.objects = {k: Object("", "").from_json(v) for k, v in dic["Objects"].items()}

    @staticmethod
    def setup_objects():
        obj = {}

        window = Object("Fenetre", "Window")
        world = Object("Monde", "World")
        world.parent = window
        window.childs["Monde"] = world

        obj["Fenetre"] = window

        return obj
