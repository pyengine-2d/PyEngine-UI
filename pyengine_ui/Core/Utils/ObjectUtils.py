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
    ],
    "Entity": [
        ["Nom", "str", "Entité"]
    ],
    "Tilemap": [
        ["Nom", "str", "Map Tile"],
        ["Position X", "int", 0],
        ["Position Y", "int", 0],
        ["Fichier JSON", "file", ""],
        ["Scale", "int", 1]
    ],
    "PositionComponent": [
        ["Nom", "str", "Position"],
        ["Position X", "int", 0],
        ["Position Y", "int", 0],
        ["Offset X", "int", 0],
        ["Offset Y", "int", 0]
    ],
    "SpriteComponent": [
        ["Nom", "str", "Sprite"],
        ["Image", "file", ""],
        ["Scale", "int", 1],
        ["Rotation", "int", 0],
        ["Flip X", "bool", False],
        ["Flip Y", "bool", False]
    ],
    "TextComponent": [
        ["Nom", "str", "Texte"],
        ["Texte", "str", ""],
        ["Scale", "int", 0]
    ],
    "PhysicsComponent": [
        ["Nom", "str", "Physique"],
        ["Affecté par Gravité", "bool", True],
        ["Friction", "int", 0],
        ["Elasticité", "int", 0],
        ["Masse", "int", 0],
        ["Solide", "bool", True]
    ],
    "MoveComponent": [
        ["Nom", "str", "Mouvement"],
        ["Direction X", "int", 0],
        ["Direction Y", "int", 0]
    ]
}

parent = {
    "World": ["Window"],
    "Entity": ["World"],
    "Tilemap": ["Tilemap"],
    "PositionComponent": ["Entity"],
    "SpriteComponent": ["Entity"],
    "TextComponent": ["Entity"],
    "PhysicsComponent": ["Entity"],
    "MoveComponent": ["Entity"]
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
        return {"Type": self.type_, "Name": self.name, "Properties": self.properties, "Script": self.script,
                "Childs": {k: v.to_json() for k, v in self.childs.items()}}

    def from_json(self, dic, parent=None):
        self.type_ = dic["Type"]
        self.name = dic["Name"]
        self.properties = dic["Properties"]
        self.parent = parent
        self.script = dic["Script"]
        self.childs = {k: Object("", "").from_json(v, self) for k, v in dic["Childs"].items()}
        return self
