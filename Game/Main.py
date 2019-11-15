import random
import json
import os

from pico2d import *
import game_framework

from Player import Player
from Land import Land


name = "MainState"

player = None
Land = None



def enter():
    global player, land
    player = Player()
    land = Land()


def exit():
    global player, land
    del player
    del land


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            player.Jump()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LCTRL:
            player.shoot()



def update():
    player.update()
    land.update()


def draw():
    clear_canvas()
    land.draw()
    player.draw()
    update_canvas()

