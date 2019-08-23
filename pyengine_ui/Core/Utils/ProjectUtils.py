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

    def get_object(self, name=None):
        for i in self.all_objects():
            if i.name == name:
                return i
        return None

    def update_objects(self, item):
        self.set_childs(self.objects[0], item, self.all_objects())

    def set_childs(self, obj, item, liste):
        obj.childs = []
        for i in range(item.childCount()):
            obj.childs.append([v for v in liste if v.name == item.child(i).text(0)][0])
            self.set_childs(obj.childs[i], item.child(i), liste)

    def all_objects(self, element=None):
        if element is None:
            elements = self.objects
        else:
            elements = element.childs
        if len(elements):
            obj = elements
            for v in elements:
                obj = [*obj, *self.all_objects(v)]
        else:
            obj = []
        return obj

    def save(self):
        objects = [v.to_json() for v in self.objects]
        file = {"Name": self.project_name, "Folder": self.project_folder, "Author": self.author,
                "Version": self.version, "Objects": objects}
        with open(os.path.join(self.project_folder, self.project_name, "project.json"), "w") as f:
            f.write(json.dumps(file, indent=4))

    def load(self, file):
        with open(file, "r", encoding="utf-8") as f:
            dic = json.load(f)
        self.project_name = dic["Name"]
        self.project_folder = dic["Folder"]
        self.author = dic["Author"]
        self.version = dic["Version"]
        self.objects = [Object("", "").from_json(v) for v in dic["Objects"]]

    @staticmethod
    def setup_objects():
        obj = []

        window = Object("Fenetre", "Window")
        world = Object("Monde", "World")
        world.parent = window
        window.childs.append(world)

        obj.append(window)

        return obj
