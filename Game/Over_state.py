import game_framework
from pico2d import *

import Main

name = "OverState"
image = None
character_dead = None
retry = None
frame = 0.0

#Player Size
SizeX = 236
SizeY = 188

# Player Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 0.3 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10

def enter():
    global image, character_dead, retry

    image = load_image('Resource/UI/Gameover.png')
    character_dead = load_image('Resource/Death.png')
    retry = load_image('Resource/UI/retry.png')


def exit():
    global image, character_dead, retry
    del(image)
    del(character_dead)
    del(retry)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(Main)


def draw():
    global frame

    clear_canvas()
    image.draw(400, 225)
    character_dead.clip_draw(int(frame) * SizeX, 0, SizeX, SizeY, 400, 200)
    if frame >= 9:
        retry.draw(600, 120)
    update_canvas()


def update():
    global frame
    if frame <= 9:
        frame = (frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10
