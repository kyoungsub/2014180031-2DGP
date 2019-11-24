import random
import json
import os

from pico2d import *
import game_framework
import game_world
import Over_state

from Player import Player
from Land import Land
from Background import Background
from Slash import Slash
from Enemy import Enemy
from Obstacle import Obstacle, Top_Obstacle, Middle_Obstacle


name = "MainState"

player = None
land = None
background = None
enemy = None
obstacle = None
Tobstacle = None
Mobstacle = None
slashs = []

score = 0
font = None

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def enter():
    global player, land, background
    background = Background()
    game_world.add_object(background, 0)
    land = Land()
    game_world.add_object(land, 0)
    player = Player()
    game_world.add_object(player, 1)

    global obstacle, Tobstacle, Mobstacle, enemy

    enemy = Enemy()
    game_world.add_object(enemy, 1)
    obstacle = Obstacle()
    game_world.add_object(obstacle, 1)
    Tobstacle = Top_Obstacle()
    game_world.add_object(Tobstacle, 1)
    Mobstacle = Middle_Obstacle()
    game_world.add_object(Mobstacle, 1)

    global font
    font = load_font('ENCR10B.TTF', 16)


def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    global slashs

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            player.Jump()
            player.frame = 1
        elif event.type == SDL_KEYUP and event.key == SDLK_SPACE:
            if player.Is_jump == True:
                player.dir = -1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LCTRL:
            player.Is_shoot = True
            slashs.append(Slash(player.x + 30, player.y))
            for i in slashs:
                game_world.add_object(i, 1)
            player.frame = 1


def update():
    global score

    for game_object in game_world.all_objects():
        game_object.update()


    #오브젝트 재생성
    if score % 100 == 0 and enemy.Died == True:
        enemy.respawn()
        game_world.add_object(enemy, 1)

    if land.land_que[3] != 0 or land.land_que[4] != 0:
        if obstacle.x <= -20:
            obstacle.respawn()

        if Tobstacle.x <= -20:
            Tobstacle.respawn()

        if Mobstacle.x <= -20:
            Mobstacle.respawn()


    #공격과 적 충돌
    if slashs != None:
        for slash in slashs:
            if collide(enemy, slash):
                if enemy.kind == 1:
                    enemy.enemy1HP -= 1
                else:
                    enemy.enemy2HP -= 1
                slashs.remove(slash)
                game_world.remove_object(slash)
                if enemy.enemy1HP == 0 or enemy.enemy2HP == 0:
                    if enemy.kind == 1:
                        score += 25
                    else:
                        score += 50
                    game_world.remove_object(enemy)
                    enemy.Died = True

    #플레이어와 적 충돌
    if collide(player, enemy):
        game_world.remove_object(enemy)
        enemy.Died = True

    #플레이어와 벽 충돌
    if player.Damaged == False:
        if collide(player, obstacle):
            player.Damaged = True
            player.Hp -= 1

        if collide(player, Tobstacle):
            player.Damaged = True
            player.Hp -= 1

        if collide(player, Mobstacle):
            player.Damaged = True
            player.Hp -= 1


    #플레이어와 바닥
    if land.land_que[1] == 0 and player.Is_jump == False:
        player.fall = True
    if land.land_que[1] == 0 and player.Is_jump == True and player.y <= 80:
        player.fall = True


    #점수
    if player.frame >= 9:
        score += 5

    #게임오버
    if player.y <= -100:
        game_framework.change_state(Over_state)
        score = 0
    if player.Hp <= 0:
        game_framework.change_state(Over_state)
        score = 0



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    font.draw(400, 200, str(score), (255, 0, 0))
    update_canvas()

