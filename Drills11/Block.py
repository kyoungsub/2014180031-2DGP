from pico2d import *
import game_framework

class Block:
    def __init__(self):
        self.image = load_image('brick180x40.png')
        self.x, self.y = 1000, 150
        self.speed = 150

    def update(self):
        if self.x > 1500:
            self.speed *= -1
        elif self.x < 180:
            self.speed *= 1

        self.x += self.speed * game_framework.frame_time

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    # fill here
    def get_bb(self):
        return self.x - 90, self.y -20, self.x + 90, self.y +20