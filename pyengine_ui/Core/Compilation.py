from pyengine_ui.Core.CompilationClasses import *

from pyengine.Utils import loggers

import time


class Compilation:
    def __init__(self, project):
        self.project = project
        self.class_function = {
            "AnimComponent": anim_class,
            "LifeComponent": life_class,
            "ControlComponent": control_class,
            "PositionComponent": position_class,
            "SpriteComponent": sprite_class,
            "TextComponent": text_class,
            "PhysicsComponent": physics_class,
            "MoveComponent": move_class,
            "Entity": entity_class,
            "Tilemap": tilemap_class,
            "World": world_class,
            "Window": window_class
        }

    def compile(self):
        plogger = loggers.get_logger("PyEngineUI")
        start = time.time()
        directory = os.path.join(self.project.project_folder, self.project.project_name)
        self.clear_files(directory)

        for i in self.project.all_objects():
            if "Component" in i.type_:
                os.makedirs(os.path.join(directory, "Components"), exist_ok=True)
                with open(os.path.join(directory, "Components", i.name.capitalize()+".py"), "w", encoding="utf-8") as f:
                    f.write(self.class_function[i.type_](self, i))
                plogger.info("Compilation " + i.name + ": Valide")
            elif i.type_ in ["Entity", "Tilemap"]:
                os.makedirs(os.path.join(directory, "Entities"), exist_ok=True)
                with open(os.path.join(directory, "Entities", i.name.capitalize()+".py"), "w", encoding="utf-8") as f:
                    f.write(self.class_function[i.type_](self, i))
                plogger.info("Compilation " + i.name + ": Valide")
            elif i.type_ == "World":
                os.makedirs(os.path.join(directory, "Worlds"), exist_ok=True)
                with open(os.path.join(directory, "Worlds", i.name.capitalize()+".py"), "w", encoding="utf-8") as f:
                    f.write(self.class_function[i.type_](self, i))
                plogger.info("Compilation " + i.name + ": Valide")
            elif i.type_ == "Window":
                with open(os.path.join(directory, "Main.py"), "w", encoding="utf-8") as f:
                    f.write(self.class_function[i.type_](self, i))
                plogger.info("Compilation " + i.name + ": Valide")
            else:
                plogger.warning(i.name+" n'a pas un type connu. ("+i.type_+")")

        plogger.info("Compilation finie en "+str(time.time() - start)+" secondes.")

    @staticmethod
    def clear_files(directory):
        for folder in ["Components", "Images", "Entities", "Worlds"]:
            if os.path.exists(os.path.join(directory, folder)):
                for i in os.listdir(os.path.join(directory, folder)):
                    if i != "__pycache__":
                        os.remove(os.path.join(directory, folder, i))
                    else:
                        for j in os.listdir(os.path.join(directory, folder, "__pycache__")):
                            os.remove(os.path.join(directory, folder, "__pycache__", j))
                        os.rmdir(os.path.join(directory, folder, "__pycache__"))
                os.rmdir(os.path.join(directory, folder))
        if os.path.exists(os.path.join(directory, "Main.py")):
            os.remove(os.path.join(directory, "Main.py"))
