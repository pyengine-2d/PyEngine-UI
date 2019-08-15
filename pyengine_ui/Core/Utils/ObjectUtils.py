properties = {
    "Window": [
        ["Nom", "str", "Fenetre"],
        ["Largeur", "int", 900],
        ["Hauteur", "int", 600],
        ["Titre", "str", "PyEngine Game"],
        ["Icon", "file", ""],
        ["FPS Max", "int", 0],
        ["Update /s", "int", 60],
        ["Debug", "bool", False]
    ],
    "World": [
        ["Nom", "str", "Monde"],
        ["Gravité X", "int", 0],
        ["Gravité Y", "int", -900]
    ]
}

parent = {
    "World": ["Window"],
}

types = parent.keys()


def get_properties(element):
    return properties.get(element, [])


def get_parent_types(element):
    return parent.get(element, [None])


class Object:
    def __init__(self, name, type_):
        self.properties = {k[0]: k[2] for k in get_properties(type_)}
        self.type_ = type_
        self.name = name
        self.childs = {}
        self.parent = None

    def set_property(self, name, value):
        if name in self.properties.keys():
            self.properties[name] = value

    def to_json(self):
        return {"Type": self.type_, "Name": self.name, "Properties": self.properties,
                "Childs": {k: v.to_json() for k, v in self.childs.items()}}

    def from_json(self, dic, parent=None):
        self.type_ = dic["Type"]
        self.name = dic["Name"]
        self.properties = dic["Properties"]
        self.parent = parent
        self.childs = {k: Object("", "").from_json(v, self) for k, v in dic["Childs"].items()}
        return self
