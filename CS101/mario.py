from cs1graphics import *
from time import sleep

_scene = None
_world = None

t = 0.2

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
        grass = Rectangle(1000, 150, Point(250, 250))
        grass.setFillColor('green')
        grass.setDepth(100)
        _scene.add(grass)

        #blocks
        block = Rectangle(40, 40, Point(200, 100))
        block.setFillColor('brown')

        qmark = Text("?", 20, Point(200, 100))
        qmark.setFontColor('Yellow')
        qmark.setDepth(48)
        _scene.add(qmark)

        block2 = block.clone()
        block2.move(40, 0)
        block.setDepth(50)
        _scene.add(block)
        _scene.add(block2)

        #pipe
        pipe = Polygon(Point(400, 150), Point(400, 160), Point(410, 160), Point(410, 320), Point(470, 320), Point(470, 160), Point(480, 160), Point(480, 150))
        pipe.setFillColor('lightgreen')
        pipe.setDepth(10)
        pipe.move(-10, 0)
        _scene.add(pipe)


class Mushroom(object):
    def __init__(self, x=200, y=92):
        mushroom = Layer()
        uppermush = Ellipse(38, 18, Point(x, y))
        uppermush.setFillColor('red')
        uppermush.setDepth(52)
        lowermush = Ellipse(35, 25, Point(x, y+8))
        lowermush.setFillColor('beige')
        lowermush.setDepth(53)
        mushroom.add(lowermush)
        mushroom.add(uppermush)
        mushroom.setDepth(52)

        self.layer = mushroom
        _scene.add(self.layer)

    def diappear(self):
        self.layer.scale(0.001)

    def move(self, x, y):
        self.layer.move(x, y)

    def arise(self):
        self.layer.setDepth(45)
        self.layer.move(0, -20)



COLOR = ['Red', 'Blue']
TYPE = ['super', 'normal']

class Mario(object):
    def __init__(self, color='Blue', type='normal'):
        assert type in TYPE and color in COLOR
        self.color = color
        self.type = type
        self.step_size = 3

    # Constructing Mario
        mario = Layer()
        # body
        body = Rectangle(33, 22, Point(200, 200))
        body.setFillColor(color)
        body.setDepth(50)
        mario.add(body)

        # face
        face = Ellipse(30, 20, Point(200, 180))
        face.setFillColor('beige')
        face.setDepth(40)
        mario.add(face)

        #hat
        hat = Polygon(Point(185, 175), Point(220, 175), Point(220, 173), Point(215, 173), Point(212, 168), Point(188, 168))
        hat.setFillColor(color)
        hat.setDepth(39)
        mario.add(hat)

        #beard
        beard = Polygon(Point(207, 183), Point(217, 183), Point(215, 180), Point(209, 180))
        beard.setFillColor('Brown')
        beard.setDepth(38)
        mario.add(beard)

        shoe = Layer()
        #left shoe
        lshoe = Rectangle(15, 6, Point(191, 215))
        lshoe.setFillColor('black')
        lshoe.setDepth(52)
        shoe.add(lshoe)

        #right shoe
        rshoe = lshoe.clone()
        rshoe.move(17, 0)
        shoe.add(rshoe)
        mario.add(shoe)

        # save alias of moveable parts
        self.layer = mario
        self.body = body
        self.hat = hat
        self.shoe = shoe
        _scene.add(self.layer)

        self.moving_part_count = 0

        if type == 'super':
            self.supermario()


    def shoe_move(self):

        if self.moving_part_count % 3 == 0:
            self.shoe.move(3, 0)
        elif self.moving_part_count % 3 == 1:
            self.shoe.move(-5,0)
        else: self.shoe.move(2,0)
        self.moving_part_count += 1
        if self.moving_part_count % 3 == 0: self.moving_part_count = 0

    def move(self,x=10,y=0):
        self.layer.move(x,y)


    def supermario(self):
        tempPt = self.body.getReferencePoint()
        self.layer.adjustReference(tempPt.getX(), tempPt.getY())
        for i in range(3):
            self.layer.scale(1.3)
            sleep(t/2)
            self.layer.scale(0.9)
            sleep(t/2)

    def walk(self,x=20):
        assert x > 0
        total_step = int(x / self.step_size)
        for i in range(total_step):
            sleep(t/4)
            self.move(self.step_size, 0)
            self.shoe_move()

def show_animation():
    sleep(t)
    mario.move(0, -50)
    mushroom.arise()

    sleep(t)
    mario.move(0, 50)
    mushroom.move(0, 8)

    for i in range(7):
        sleep(t/2)
        mushroom.move(10, 0)
        mario.move(10, 0)
        mario.shoe_move()
        sleep(t/2)
        mario.shoe_move()

    sleep(t/2)
    mushroom.move(0, 50)
    mario.move(10, 0)
    mario.shoe_move()
    sleep(t/2)
    mario.shoe_move()

    sleep(t)
    mushroom.move(0, 50)

    sleep(t/2)
    mushroom.diappear()
    sleep(t/2)
    mario.supermario()

    for i in range(6):
        sleep(t/2)
        mario.move(10, 0)
        mario.shoe_move()
        sleep(t/2)
        mario.shoe_move()

    for i in range(2):
        sleep(t)
        mario.move(28, -60)

    for i in range(1):
        sleep(t)
        mario.move(32, 40)

    sleep(2*t)
    for i in range(4):
        sleep(t)
        mario.move(0, 25)
        
def interactive_example():
    while True:
        e = _scene.wait()
        d = e.getDescription()
        if d == "keyboard":
            k = e.getKey()
            if k == "q":
                _scene.close()
                break
            elif k == "w":
                mario.walk(20)
            elif k == "r":
                mario.walk(40)
            elif k == "j":
                mario.move(0, -50)
                sleep(t)
                mario.move(0, 50)

create_world()
mario = Mario('Blue', 'normal')
mushroom = Mushroom(200, 92)

show_animation()
# interactive_example()


