import game_framework
from pico2d import *
import game_world

#Player Size
SizeX = 147
SizeY = 176

# Player Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10

Image_timer = 0.0

class Player:

    def __init__(self):
        self.x, self.y = 200, 80
        self.image = load_image('Resource/Player_animation_sheet.png')
        self.dir = 1
        self.Jump_Maximum = 250
        self.frame = 0
        self.timer = 0      #이동거리에따라 땅 삭제를 위해
        self.dir = 1
        self.Hp = 5
        self.Is_jump = False
        self.Is_shoot = False
        self.fall = False
        self.Damaged = False


    def get_bb(self):
        return self.x - 40, self.y - 50, self.x + 50, self.y + 50

    def Jump(self):
        self.Is_jump =True

    def update(self):
        global Image_timer

        #점프
        if self.Is_jump == True:
            if self.y > self.Jump_Maximum + 80:
                self.dir = -1
            if self.y <= 80:
                self.dir = 1
                self.Is_jump = False
            self.y += self.dir * 200 * game_framework.frame_time

        #점프 애니메이션 최적화
            self.frame = (self.frame + FRAMES_PER_ACTION * 0.7 * game_framework.frame_time) % 10
        else:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10

        #공격
        if self.Is_shoot == True and self.frame >= 9:
            self.Is_shoot = False

        #낙하
        if self.fall == True:
            self.y -= 200 * game_framework.frame_time

        #데미지시 깜빡임
        if self.Damaged == True:
            Image_timer = (Image_timer + 1)
            if Image_timer == 180:
                self.Damaged = False
                Image_timer = 0



    def draw(self):
        global Image_timer

        if self.Damaged == True:
            if (Image_timer%50) >= 10:
                if self.Is_jump == True:
                    self.image.clip_draw(int(self.frame) * SizeX, SizeY, SizeX, SizeY, self.x, self.y)
                elif self.Is_shoot == True:
                    self.image.clip_draw(int(self.frame) * SizeX, SizeY * 0, SizeX, SizeY, self.x, self.y)
                else:
                    self.image.clip_draw(int(self.frame) * SizeX, SizeY * 2, SizeX, SizeY, self.x, self.y)
        else:
            if self.Is_jump == True:
                self.image.clip_draw(int(self.frame) * SizeX, SizeY, SizeX, SizeY, self.x, self.y)
            elif self.Is_shoot == True:
                self.image.clip_draw(int(self.frame) * SizeX, SizeY * 0, SizeX, SizeY, self.x, self.y)
            else:
                self.image.clip_draw(int(self.frame) * SizeX, SizeY * 2, SizeX, SizeY, self.x, self.y)



