import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball, BigBall
from Block import Block

name = "MainState"

boy = None
grass = None
block = None
balls = []
big_balls = []


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    global balls
    balls = [Ball() for i in range(10)] + [BigBall() for i in range(10)]
    for i in range(20):
        game_world.add_object(balls[i], 1)

    global block
    block = Block()
    game_world.add_object(block, 1)


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
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for ball in balls:
        if collide(boy, ball):
            balls.remove(ball)
            game_world.remove_object(ball)

    for ball in balls:
        if collide(grass, ball):
            ball.stop()

    for ball in balls:
        if collide(block, ball):
            ball.stop()
            ball.x += block.speed * game_framework.frame_time

    if collide(block, boy):
        if boy.speed <= 0 and boy.y >= 170:
            boy.speed = 0
            boy.y = block.y + 50
            boy.x += block.speed * game_framework.frame_time




def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






