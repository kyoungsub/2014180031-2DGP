from pico2d import *
import game_world
import game_framework


class Slash:
    image = None

    def __init__(self, px, py):
        if self.image == None:
            self.image = load_image('Resource/slash.png')
        self.x, self.y, self.shoot_speed = px + 30, py, 100



    def get_bb(self):
        # fill here
        return self.x - 70, self.y - 25, self.x + 70, self.y + 25

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.shoot_speed * game_framework.frame_time
