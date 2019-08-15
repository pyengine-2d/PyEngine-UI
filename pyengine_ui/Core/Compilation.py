import os


class Compilation:
    def __init__(self, project):
        self.project = project

    def compile(self):
        directory = os.path.join(self.project.project_folder, self.project.project_name)
        for i in self.project.all_objects().values():
            if "Component" in i.type_:
                os.makedirs(os.path.join(directory, "Components"), exist_ok=True)
                with open(os.path.join(directory, "Components", i.name.capitalize()+".py"), "w") as f:
                    if i.type_ == "PositionComponent":
                        f.write(self.position_class(i))
                    elif i.type_ == "SpriteComponent":
                        f.write(self.sprite_class(i))
                    elif i.type_ == "TextComponent":
                        f.write(self.text_class(i))
                    elif i.type_ == "PhysicsComponent":
                        f.write(self.physics_class(i))
                    else:
                        f.write(self.move_class(i))
                print(i.name+" a été compilé avec succès")
            elif i.type_ in ["Entity", "Tilemap"]:
                os.makedirs(os.path.join(directory, "Entities"), exist_ok=True)
                with open(os.path.join(directory, "Entities", i.name.capitalize()+".py"), "w") as f:
                    if i.type_ == "Entity":
                        f.write(self.entity_class(i))
                    else:
                        f.write(self.tilemap_class(i))
                print(i.name+" a été compilé avec succès")
            elif i.type_ == "World":
                os.makedirs(os.path.join(directory, "Worlds"), exist_ok=True)
                with open(os.path.join(directory, "Worlds", i.name.capitalize()+".py"), "w") as f:
                    f.write(self.world_class(i))
                print(i.name+" a été compilé avec succès")
            elif i.type_ == "Window":
                with open(os.path.join(directory, "Main.py"), "w") as f:
                    f.write(self.window_class(i))
                print(i.name+" a été compilé avec succès.")
            else:
                raise TypeError("Unknown type for compilation : "+i.type_)

    def position_class(self, pos):
        pos_x = str(pos.properties["Position X"])
        pos_y = str(pos.properties["Position Y"])
        off_x = str(pos.properties["Offset X"])
        off_y = str(pos.properties["Offset Y"])

        text = "from pyengine.Components import PositionComponent\nfrom pyengine.Utils import Vec2\n\n\n"
        text += "class "+pos.name+"(PositionComponent):\n"
        text += "    def __init__(self):\n"
        text += "        super("+pos.name+", self).__init__(Vec2("+pos_x+", "+pos_y+"), Vec2("+off_x+", "+off_y+"))\n"
        return text

    def sprite_class(self, sprite):
        image = str(sprite.properties["Image"])
        scale = str(sprite.properties["Scale"])
        rot = str(sprite.properties["Rotation"])
        flipx = str(sprite.properties["Flip X"])
        flipy = str(sprite.properties["Flip Y"])

        text = "from pyengine.Components import SpriteComponent\n\n\n"
        text += "class "+sprite.name+"(SpriteComponent):\n"
        text += "    def __init__(self):\n"
        text += "        super("+sprite.name+', self).__init__("'+image+'", '+scale+", "+rot+", "+flipx+", "+flipy+")\n"
        return text

    def physics_class(self, phys):
        agravity = str(phys.properties["Affecté par Gravité"])
        fric = str(phys.properties["Friction"])
        elas = str(phys.properties["Elasticité"])
        mass = str(phys.properties["Masse"])
        solid = str(phys.properties["Solide"])

        text = "from pyengine.Components import PhysicsComponent\n\n\n"
        text += "class "+phys.name+"(PhysicsComponent):\n"
        text += "    def __init__(self):\n"
        text += "        super("+phys.name+", self).__init__("+agravity+", "+fric+", "+elas+", "+mass+", "+solid+")\n"
        return text

    def move_class(self, move):
        dirx = str(move.properties["Direction X"])
        diry = str(move.properties["Direction Y"])

        text = "from pyengine.Components import MoveComponent\nfrom pyengine.Utils import Vec2\n\n\n"
        text += "class "+move.name+"(MoveComponent):\n"
        text += "    def __init__(self):\n"
        text += "        super("+move.name+", self).__init__(Vec2("+dirx+", "+diry+"))\n"
        return text

    def text_class(self, txt):
        texte = str(txt.properties["Texte"])
        scale = str(txt.properties["Scale"])

        text = "from pyengine.Components import TextComponent\n\n\n"
        text += "class "+txt.name+"(TexteComponent):\n"
        text += "    def __init__(self):\n"
        text += "        super("+txt.name+', self).__init__("'+texte+'", scale='+scale+")\n"
        return text

    def tilemap_class(self, tilemap):
        pos_x = str(tilemap.properties["Position X"])
        pos_y = str(tilemap.properties["Position Y"])
        file = str(tilemap.properties["Fichier JSON"])
        scale = str(tilemap.properties["Scale"])

        text = "from pyengine.Entities import Tilemap\nfrom pyengine.Utils import Vec2\n"
        if len(tilemap.childs.values()):
            for i in tilemap.childs.values():
                text += "from Components."+i.name.capitalize()+" import "+i.name+"\n"
        text += "\n\nclass "+tilemap.name+"(Tilemap):\n"
        text += "    def __init__(self):\n"
        text += "        super("+tilemap.name+", self).__init__(Vec2("+pos_x+", "+pos_y+"), "+file+", "+scale+")\n"
        if len(tilemap.childs.values()):
            for i in tilemap.childs.values():
                text += "        self.add_component("+i.name+"())\n"
        return text

    def entity_class(self, entity):
        text = "from pyengine.Entities import Entity\n"
        if len(entity.childs.values()):
            for i in entity.childs.values():
                text += "from Components."+i.name.capitalize()+" import "+i.name+"\n"
        text += "\n\nclass "+entity.name+"(Entity):\n"
        text += "    def __init__(self):\n"
        text += "        super("+entity.name+", self).__init__()\n"
        if len(entity.childs.values()):
            for i in entity.childs.values():
                text += "        self.add_component("+i.name+"())\n"
        return text

    def world_class(self, world):
        gravity_x = str(world.properties["Gravité X"])
        gravity_y = str(world.properties["Gravité Y"])

        text = "from pyengine import World\n"
        if len(world.childs.values()):
            text += "from pyengine.Systems import EntitySystem\n"
            for i in world.childs.values():
                text += "from Entities."+i.name.capitalize()+" import "+i.name+"\n"
        text += "\n\nclass "+world.name+"(World):\n"
        text += "    def __init__(self, window):\n"
        text += "        super("+world.name+", self).__init__(window, ["+gravity_x+", "+gravity_y+"])\n"
        if len(world.childs.values()):
            text += "        self.esys = self.get_system(EntitySystem)\n"
            for i in world.childs.values():
                text += "        self.esys.add_entity("+i.name+"())\n"
        return text

    def window_class(self, window):
        largeur = str(window.properties["Largeur"])
        hauteur = str(window.properties["Hauteur"])
        titre = str(window.properties["Titre"])
        icon = str(window.properties["Icon"])
        if window.properties["FPS Max"] == 0:
            fps = str(None)
        else:
            fps = str(window.properties["FPS Max"])
        update = str(window.properties["Update /s"])
        debug = str(window.properties["Debug"])

        text = "from pyengine import Window\n"
        if len(window.childs.values()):
            for i in window.childs.values():
                text += "from Worlds."+i.name.capitalize()+" import "+i.name+"\n"
        text += "\n\nclass "+window.name+"(Window):\n"
        text += "    def __init__(self):\n"
        text += "        super("+window.name+", self).__init__("+largeur+", "+hauteur
        if titre != "":
            text += ', title="'+titre+'"'
        if icon != "":
            text += ', icon="'+icon + '"'
        text += ", limit_fps="+fps+", update_rate="+update+", debug="+debug+")\n"
        if len(window.childs.values()):
            i = None
            for i in window.childs.values():
                text += "        self."+i.name.lower()+" = "+i.name+"(self)\n"
            text += "        self.world = self."+i.name.lower()+"\n"
        text += "        self.run()\n\n\n"
        text += window.name+"()"
        return text
