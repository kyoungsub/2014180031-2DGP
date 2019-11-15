import game_framework
import random
from pico2d import *
from Player import Player

class Land:
    def __int__(self):
        self.image1 = load_image('Resource/floor/1stage/floor1.png')
        self.image2 = load_image('Resource/floor/1stage/floor2.png')
        self.image3 = load_image('Resource/floor/1stage/floor3.png')
        self.land_que = [1, 1, 1, 1, 1]
        self.player_pass = False


    def update(self):
        #땅 빈공간 삭제후 추가
        if self.player_pass == True:
            self.land_que.pop(1)
            self.land_que.append(random.randint(0, 1))
            self.player_pass = False

    def draw(self):
        for i in range(4):
            if self.land_que[i] == 1:
                self.image1.draw(100 * i, 15)

    def get_bb(self):
        return 0, 0, 800-1, 30