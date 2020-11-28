from cs1graphics import *
from time import sleep

_scene = None
_world = None

def create_world():
    global _scene, _world
    if _scene:
        raise RuntimeError("A world already exists!")
    _world = _World(500, 300)
    _scene = Canvas(_world.width, _world.height)
    _scene.setTitle("Mario World")
    _world.draw_scene()

class _World(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw_scene(self):
        """
        draw background here
        Don't forget _scene.add(name)
        """
        pass


"""
define your own objects, e.g. Mario and Mushroom

class Mushroom (object):
    def __init__(self, x, y):
        mushroom = Layer()

        uppermush = Ellipse(38, 18, Point(x, y))
        uppermush.setFillColor('red')
        uppermush.setDepth(52)
        mushroom.add(lowermush)

        lowermush = Ellipse(35, 25, Point(x, y+8))
        lowermush.setFillColor('beige')
        lowermush.setDepth(53)
        mushroom.add(uppermush)

        mushroom.setDepth(52)

        self.layer = mushroom   # save mushroom shape in the class
        _scene.add(self.layer)  # add to global Canvas

class Mario (object):
    def __init__(self, ...
        self.layer = Layer()
        ...
        _scene.add(self.layer)
"""



create_world()
# define your objects, e.g. mario = Mario('blue', 'normal')

# write your animation scenario here
