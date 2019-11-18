import random
import json
import os

from pico2d import *
import game_framework
import game_world

from Player import Player
from Land import Land
from Background import Background
from Slash import Slash


name = "MainState"

player = None
land = None
background = None
slash = []

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def enter():
    global player, land, background, slash
    player = Player()
    game_world.add_object(player, 1)
    land = Land()
    game_world.add_object(land, 0)
    background = Background()
    game_world.add_object(player, 0)


def exit():
    game_world.clear()


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
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

