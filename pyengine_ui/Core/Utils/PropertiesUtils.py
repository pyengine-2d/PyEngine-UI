properties = {
    "Window": {
        "width": "int",
        "height": "int",
        "title": "str",
        "debug": "bool"
    }
}


def get_properties(element):
    return properties.get(element, {})


class Object:
    def __init__(self, type_):
        self.properties = {k: None for k in get_properties(type_).keys()}
        self.type_ = type_

    def set_properties(self, nom, value):
        if nom in self.properties.keys():
            self.properties[nom] = value
