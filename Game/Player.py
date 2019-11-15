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

# Player Event
CTRL_DOWN, CTRL_UP,SPACE = range(3)

key_event_table = {
    (SDL_KEYDOWN, SDLK_LCTRL): CTRL_DOWN,
    (SDL_KEYUP, SDLK_LCTRL): CTRL_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


class RunState:
    @staticmethod
    def enter(player, event):
        player.dir = clamp(-1, player.velocity, 1)

    @staticmethod
    def exit(player, event):
        if event == SPACE:
            player.speed = 5

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10

    @staticmethod
    def draw(player):
        player.image.clip_draw(int(player.frame) * SizeX, SizeY, SizeX, SizeY, player.x, player.y)

class JumpState:
    @staticmethod
    def enter(player, event):
        player.dir = clamp(-1, player.velocity, 1)

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10

    @staticmethod
    def draw(player):
        player.image.clip_draw(int(player.frame) * SizeX, SizeY, SizeX, SizeY, player.x, player.y)


next_state_table = {
    RunState: {CTRL_DOWN: RunState, CTRL_UP: RunState, SPACE: JumpState},
    JumpState: {CTRL_DOWN: JumpState, CTRL_UP: JumpState, SPACE: JumpState}
}




class Player:

    def __init__(self):
        self.x, self.y = 200, 90
        self.image = load_image('Resource/Player_animation.png')
        self.dir = 1
        self.Jump_speed = 0
        self.frame = 0
        self.timer = 0      #이동거리에따라 땅 삭제를 위해

    def get_bb(self):
        return self.x - (SizeX/2), self.y - (SizeY/2), self.x + (SizeX/2), self.y + (SizeY/2)

    def fire(self):
        slash = Ball(self.x, self.y, self.dir * RUN_SPEED_PPS * 10)
        game_world.add_object(slash, 1)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
