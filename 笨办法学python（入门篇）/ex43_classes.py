class Scene():
    def enter(self):
        pass

class Engine():
    def __init__(self, scene_map):
        pass
    def play(self):
        pass

class Death():

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapPod(Scene):

    def enter(self):
        pass

class Map():

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()