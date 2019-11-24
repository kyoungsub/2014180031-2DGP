import game_framework
from pico2d import *

import Main

name = "TitleState"
image = None
blink_text = None
image_timer = 0.0


def enter():
    global image, blink_text, image_timer

    image = load_image('Resource/UI/Main.png')
    blink_text = load_image('Resource/UI/PETP.png')
    image_timer = 0.0


def exit():
    global image, blink_text
    del(image)
    del(blink_text)


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
    global image_timer

    clear_canvas()
    image.draw(400, 225)
    if image_timer >= 10:
        blink_text.draw(550, 175)
    update_canvas()


def update():
    global image_timer

    image_timer = (image_timer + game_framework.frame_time * 100) % 50
