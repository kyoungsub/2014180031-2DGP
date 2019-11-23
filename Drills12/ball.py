import random
import math
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
from pico2d import *
import main_state


class Ball:
    def __init__(self):
        self.x, self.y = random.randint(range(100,400)), random.randint(range(100,400))
        self.image = load_image('ball21x21.png')
        self.Hp = 50

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)

class BigBall(Ball):
    def __init__(self):
        BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(range(100, 400)), random.randint(range(100, 400))
        BigBall.Hp = 100

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20