import game_framework
import random
from pico2d import *

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


class Land:

    def __init__(self):
        self.image1 = load_image('Resource/floor/1stage/floor1.png')
        self.image2 = load_image('Resource/floor/1stage/floor2.png')
        self.image3 = load_image('Resource/floor/1stage/floor3.png')
        self.land_que = [1, 1, 0, 1, 1]
        self.location = 200
        self.fixed_pos = 0
        self.player_pass = False

    def update(self):
        self.fixed_pos -= 200 * game_framework.frame_time
        #땅 빈공간 삭제후 추가
        if self.fixed_pos <= -200:
            self.land_que.pop(0)
            self.land_que.append(random.randint(0, 1))
            if self.land_que[3] == 0:
                self.land_que[4] = 1
            self.fixed_pos = 0

    def draw(self):
        for i in range(5):
            if self.land_que[i] == 1:
                self.image1.draw(self.location * i + self.fixed_pos + 100, 15)

    def get_bb(self):
        return 0, 0, 800-1, 30