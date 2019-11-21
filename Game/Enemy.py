from pico2d import *
import game_world
import game_framework

# Player Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10

class Enemy:
    image1 = None
    image2 = None

    def __init__(self, px, py):
        if self.image1 == None:
            self.image1 = load_image('Resource/Object/Monster/Stump1.png')
        if self.image2 == None:
            self.image2 = load_image('Resource/Object/Monster/Stump2.png')
        self.x, self.y, self.speed = px + 30, py, 100
        self.HP = 3 #3대맞으면 사망


    def get_bb(self):
        # fill here
        return self.x - 70, self.y - 25, self.x + 70, self.y + 25

    def Update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10

    def draw(self):
        self.image1.draw(self.x, self.y)

    def update(self):
        self.x += self.speed * game_framework.frame_time
