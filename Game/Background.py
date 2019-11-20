import game_framework
from pico2d import *

class Background:
    def __init__(self):
        self.image1 = load_image('Resource/Background/1stage/back1-1.png')
        self.image2 = load_image('Resource/Background/1stage/back1-2.png')
        self.image3 = load_image('Resource/Background/1stage/back1-3.png')
        self.land_que = [1, 1]
        self.location = 800
        self.fixed_pos = 0


    def update(self):
        self.fixed_pos -= 200 * game_framework.frame_time
        if self.fixed_pos <= -800:
            self.fixed_pos = 0



    def draw(self):
        for i in range(2):
            self.image1.draw(self.location * i + self.fixed_pos + 400, 300)

    def get_bb(self):
        return 0, 0, 800-1, 30