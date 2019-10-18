import game_framework
from pico2d import *

import main_state

name = "Pause State"
image = None
image_timer = 0.0


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)


def handle_events():
    pass


def draw():
    global image
    clear_canvas()
    game_framework.stack[-2].draw()
    if(image_timer > 50):
        image.draw(400, 300)
    update_canvas()


def update():
    global image_timer
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()
    image_timer += image_timer % 100 +0.01


def pause():
    pass


def resume():
    pass
