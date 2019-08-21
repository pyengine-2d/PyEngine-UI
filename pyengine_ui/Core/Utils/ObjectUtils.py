properties = {
    "Window": [
        ["Nom", "str", "Fenetre"],
        ["Largeur", "int", 900],
        ["Hauteur", "int", 600],
        ["Couleur", "color", [0, 0, 0]],
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
        ["Nom", "str", "Entite"]
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
        ["Scale", "int", 1],
        ["Couleur", "color", [255, 255, 255]],
        ["Font", "colorNone", None],
        ["Nom Police", "str", "arial"],
        ["Taille Police", "int", 15],
        ["Italique", "bool", False],
        ["Gras", "bool", False],
        ["Souligné", "bool", False]
    ],
    "PhysicsComponent": [
        ["Nom", "str", "Physique"],
        ["Affecté par Gravité", "bool", True],
        ["Friction", "int", 1],
        ["Elasticité", "int", 1],
        ["Masse", "int", 1],
        ["Solide", "bool", True],
        ["Rotation", "bool", True],
        ["Callback", "str", ""]
    ],
    "MoveComponent": [
        ["Nom", "str", "Mouvement"],
        ["Direction X", "int", 0],
        ["Direction Y", "int", 0]
    ],
    "ControlComponent": [
        ["Nom", "str", "Controle"],
        ["Type de Controle", "list|FOURDIRECTION, CLASSICJUMP, CLICKFOLLOW, LEFTRIGHT, UPDOWN, MOUSEFOLLOW",
         "FOURDIRECTION"],
        ["Vitesse", "int", 20],
        ["Controle Haut", "str", "UP"],
        ["Controle Gauche", "str", "LEFT"],
        ["Controle Droit", "str", "RIGHT"],
        ["Controle Bas", "str", "DOWN"]
    ],
    "LifeComponent": [
        ["Nom", "str", "Life"],
        ["Vie Max", "int", 100],
        ["Callback", "str", ""]
    ],
    "AnimComponent": [
        ["Nom", "str", "Anim"],
        ["Timer", "int", 20],
        ["Images", "files", ""],
        ["Flip X", "bool", False],
        ["Flip Y", "bool", False]
    ],
    "AnimatedImage": [
        ["Nom", "str", "AnimImage"],
        ["Position X", "int", 0],
        ["Position Y", "int", 0],
        ["Images", "files", ""],
        ["Timer", "int", 20],
        ["Taille X", "int", 0],
        ["Taille Y", "int", 0]
    ],
    "Button": [
        ["Nom", "str", "Bouton"],
        ["Position X", "int", 0],
        ["Position Y", "int", 0],
        ["Texte", "str", ""],
        ["Commande", "str", ""],
        ["Taille X", "int", 100],
        ["Taille Y", "int", 40],
        ["Image", "fileNone", None]
    ],
    "Checkbox": [
        ["Nom", "str", "Boite"],
        ["Position X", "int", 0],
        ["Position Y", "int", 0],
        ["Texte", "str", ""],
        ["Coché", "bool", False],
        ["Scale", "int", 1]
    ],
    "Console": [
        ["Nom", "str", "Console"],
        ["Position X", "int", 0],
        ["Position Y", "int", 0],
        ["Largeur", "int", 600]
    ],
    "Entry": [
        ["Nom", "str", "Entrée"],
        ["Position X", "int", 0],
        ["Position Y", "int", 0],
        ["Largeur", "int", 200],
        ["Image", "fileNone", None],
        ["Couleur", "color", [255, 255, 255]],
        ["Nom Police", "str", "arial"],
        ["Taille Police", "int", 15],
        ["Italique", "bool", False],
        ["Gras", "bool", False],
        ["Souligné", "bool", False]
    ],
    "Image": [
        ["Nom", "str", "Image"],
        ["Position X", "int", 0],
        ["Position Y", "int", 0],
        ["Image", "file", ""],
        ["Taille X", "int", 0],
        ["Taille Y", "int", 0]
    ],
    "Label": [
        ["Nom", "str", "Texte"],
        ["Position X", "int", 0],
        ["Position Y", "int", 0],
        ["Texte", "str", ""],
        ["Couleur", "color", [255, 255, 255]],
        ["Font", "colorNone", None],
        ["Nom Police", "str", "arial"],
        ["Taille Police", "int", 15],
        ["Italique", "bool", False],
        ["Gras", "bool", False],
        ["Souligné", "bool", False]
    ],
    "MultilineLabel": [
        ["Nom", "str", "Texte"],
        ["Position X", "int", 0],
        ["Position Y", "int", 0],
        ["Texte", "str", ""],
        ["Couleur", "color", [255, 255, 255]],
        ["Font", "colorNone", None],
        ["Nom Police", "str", "arial"],
        ["Taille Police", "int", 15],
        ["Italique", "bool", False],
        ["Gras", "bool", False],
        ["Souligné", "bool", False]
    ],
    "ProgressBar": [
        ["Nom", "str", "Texte"],
        ["Position X", "int", 0],
        ["Position Y", "int", 0],
        ["Taille X", "int", 150],
        ["Taille Y", "int", 10],
        ["Image Fond", "fileNone", None],
        ["Image Barre", "fileNone", None]
    ],
    "Selector": [
        ["Nom", "str", "Selecteur"],
        ["Position X", "int", 0],
        ["Position Y", "int", 0],
        ["Mots (séparé d'un -)", "str", "Exemple1-Exemple2"]
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
    "MoveComponent": ["Entity"],
    "ControlComponent": ["Entity"],
    "LifeComponent": ["Entity"],
    "AnimComponent": ["Entity"],
    "AnimatedImage": ["World"],
    "Button": ["World"],
    "Checkbox": ["World"],
    "Console": ["World"],
    "Entry": ["World"],
    "Image": ["World"],
    "Label": ["World"],
    "MultilineLabel": ["World"],
    "ProgressBar": ["World"],
    "Selector": ["World"]
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
        self.childs = []
        self.parent = None
        self.script = ""

    def set_property(self, name, value):
        if name in self.properties.keys():
            self.properties[name] = value

    def to_json(self):
        return {"Type": self.type_, "Name": self.name, "Properties": self.properties, "Script": self.script,
                "Childs": [v.to_json() for v in self.childs]}

    def from_json(self, dic, parent=None):
        self.type_ = dic["Type"]
        self.name = dic["Name"]
        self.properties = dic["Properties"]
        self.parent = parent
        self.script = dic["Script"]
        self.childs = [Object("", "").from_json(v, self) for v in dic["Childs"]]
        return self
