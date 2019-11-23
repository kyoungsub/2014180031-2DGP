from pico2d import *
import game_world
import game_framework


class Obstacle:
    def __init__(self):
        self.speed = 100

    def Update(self):
        self.x -= self.speed * game_framework.frame_time

    def draw(self):
        self.image1.draw(self.x, self.y)

    def update(self):
        self.x += self.speed * game_framework.frame_time


class Obj_stump(Obstacle):
    def __init__(self):
        self.x, self.y = 800, 80
        self.Obj_stump1 = load_image('Resource/Object/1stage/stump_160_88.png')
        self.Obj_stump2 = load_image('Resource/Object/1stage/stump_118_100.png')

    def get_bb(self):
        return self.x - 80, self.y - 44, self.x + 80, self.y + 44



