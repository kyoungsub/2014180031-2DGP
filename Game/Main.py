import random
import json
import os

from pico2d import *
import game_framework

from Player import Player
from Land import Land
from Background import Background


name = "MainState"

player = None
land = None
background = None


def enter():
    global player, land, background
    player = Player()
    land = Land()
    background = Background()


def exit():
    global player, land, background
    del player
    del land
    del background


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
            player.frame = 0
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LCTRL:
            player.shoot()


def update():
    player.update()
    land.update()
    background.update()


def draw():
    clear_canvas()
    background.draw()
    land.draw()
    player.draw()
    update_canvas()

