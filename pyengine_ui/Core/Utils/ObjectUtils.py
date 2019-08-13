properties = {
    "Window": [
        ["Largeur", "int", 900],
        ["Hauteur", "int", 600],
        ["Titre", "str", "PyEngine Game"],
        ["Icon", "file", ""],
        ["FPS Max", "int", 0],
        ["Update /s", "int", 60],
        ["Debug", "bool", False]
    ],
    "World": [
        ["Gravité X", "int", 0],
        ["Gravité Y", "int", -900]
    ]
}


def get_properties(element):
    return properties.get(element, [])


class Object:
    def __init__(self, type_):
        self.properties = {k[0]: k[2] for k in get_properties(type_)}
        self.type_ = type_

    def set_property(self, nom, value):
        if nom in self.properties.keys():
            self.properties[nom] = value
