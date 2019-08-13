properties = {
    "Window": {
        "Largeur": "int",
        "Hauteur": "int",
        "Titre": "str",
        "Icon": "file",
        "FPS Max": "int",
        "Update /s": "int",
        "Debug": "bool"
    }
}


def get_properties(element):
    return properties.get(element, {})


class Object:
    def __init__(self, type_):
        self.properties = {k: None for k in get_properties(type_).keys()}
        self.type_ = type_

    def set_property(self, nom, value):
        if nom in self.properties.keys():
            self.properties[nom] = value
