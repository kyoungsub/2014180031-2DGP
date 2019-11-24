from pico2d import *
import game_world
import random
import game_framework

# Player Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 0.3 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10


class Enemy:
    image1 = None
    image2 = None

    def __init__(self):
        if self.image1 == None:
            self.image1 = load_image('Resource/Object/Monster/Stump1.png')
        if self.image2 == None:
            self.image2 = load_image('Resource/Object/Monster/Stump2.png')
        self.x, self.y, self.speed = 800, 50, 100
        self.enemy1HP = 1 #3대맞으면 사망
        self.enemy2HP = 2 #5대
        self.frame = 0
        self.Is_hit = False
        self.Died = False
        self.kind = random.randint(1, 2)

    def get_bb(self):
        # fill here
        return self.x - 35, self.y - 40, self.x + 35, self.y + 40

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.x -= self.speed * game_framework.frame_time

    def respawn(self):
        self.x = 1000
        self.kind = random.randint(1, 2)
        self.enemy1HP = 1
        self.enemy2HP = 2
        self.Died = False

    def draw(self):
        if self.kind == 1:
            self.image1.clip_draw(int(self.frame) * 75, 213, 70, 80, self.x, self.y)
        elif self.kind == 2:
            self.image2.clip_draw(int(self.frame) * 85, 160, 85, 90, self.x, self.y)

