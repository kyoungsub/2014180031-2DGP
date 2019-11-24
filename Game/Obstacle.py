from pico2d import *
import game_world
import game_framework


class Obstacle:
    def __init__(self):
        self.x, self.y = 800, 50
        self.speed = 200
        self.Obstacle_que = [0, 0, 0, 0, 1]

        self.Obj1 = load_image('Resource/Object/1stage/stump_160_88.png')
        self.Obj2 = load_image('Resource/Object/1stage/stump_118_100.png')

    def get_bb(self):
        return self.x - 50, self.y - 30, self.x + 40, self.y + 30

    def respawn(self):
        self.x = 900

    def update(self):
        self.x -= self.speed * game_framework.frame_time

    def draw(self):
        self.Obj1.draw(self.x, self.y)


class Middle_Obstacle(Obstacle):
    def __init__(self):
        self.x, self.y = 3000, 400
        self.speed = 200
        self.Obj1 = load_image('Resource/Object/1stage/root_116_133.png')

    def respawn(self):
        self.x = 1100

    def get_bb(self):
        return self.x - 50, self.y -60, self.x +40, self.y + 50

class Top_Obstacle(Obstacle):
    def __init__(self):
        self.x, self.y = 1500, 100
        self.speed = 200
        self.Obj1 = load_image('Resource/Object/1stage/tree_130_194.png')

    def respawn(self):
        self.x = 1300

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 40, self.y + 45




