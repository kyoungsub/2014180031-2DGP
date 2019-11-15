import game_framework
from pico2d import *
from Slash import Slash
import game_world

#Player Size
SizeX = 294
SizeY = 353

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Player Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10


class Player:

    def __init__(self):
        self.x, self.y = 200, 90
        self.image = load_image('Resource/Player_animation.png')
        self.dir = 1
        self.Jump_speed = 0
        self.frame = 0
        self.timer = 0      #이동거리에따라 땅 삭제를 위해
        self.Is_jump = False
        self.Is_shoot = False


    def get_bb(self):
        return self.x - (SizeX/2), self.y - (SizeY/2), self.x + (SizeX/2), self.y + (SizeY/2)

    def shoot(self):
        self.Is_shoot = True
        slash = Slash(self.x, self.y)
        game_world.add_object(slash, 1)

    def Jump(self):
        self.Is_jump =True

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10

    def draw(self):
        if self.Is_jump == True:
            self.image.clip_draw(int(self.frame) * SizeX, SizeY, SizeX, SizeY, self.x, self.y)
        elif self.Is_shoot == True:
            self.image.clip_draw(int(self.frame) * SizeX * 2, SizeY, SizeX, SizeY, self.x, self.y)


