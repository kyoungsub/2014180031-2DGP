import game_framework
from pico2d import *
from Slash import Slash
import game_world

#Player Size
SizeX = 147
SizeY = 176

# Player Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10


class Player:

    def __init__(self):
        self.x, self.y = 200, 80
        self.image = load_image('Resource/Player_animation_sheet.png')
        self.dir = 1
        self.Jump_Maximum = 150
        self.frame = 0
        self.timer = 0      #이동거리에따라 땅 삭제를 위해
        self.dir = 1
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
        #점프
        if self.Is_jump == True:
            if self.y > self.Jump_Maximum + 80:
                self.dir = -1
            self.y += self.dir * 200 * game_framework.frame_time
            if self.y <= 80:
                self.dir = 1
                self.Is_jump = False

        #프레임 고정
            if self.frame <= 4 and self.y <= self.Jump_Maximum and dir == -1:
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10
            elif self.y >= self.Jump_Maximum + 80 and dir == 1:
                self.frame = 5
            elif self.frame >= 5 and self.y <= self.Jump_Maximum and dir == -1:
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10

        #공격
        if self.Is_shoot == True and self.frame == 0:
            self.Is_shoot = False

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10


    def draw(self):
        if self.Is_jump == True:
            self.image.clip_draw(int(self.frame) * SizeX, SizeY, SizeX, SizeY, self.x, self.y)
        elif self.Is_shoot == True:
            self.image.clip_draw(int(self.frame) * SizeX, SizeY * 0, SizeX, SizeY, self.x, self.y)
        else:
            self.image.clip_draw(int(self.frame) * SizeX, SizeY * 2, SizeX, SizeY, self.x, self.y)


