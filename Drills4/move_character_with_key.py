from pico2d import *

def handle_events():
    global running
    global x
    global dir
    global animation_key
    events = get_events()


    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                animation_key=1
            elif event.key == SDLK_LEFT:
                dir -= 1
                animation_key =1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                animation_key =0
            elif event.key == SDLK_LEFT:
                dir += 1
                animation_key=0

open_canvas()
grass = load_image('grass.png')
character= load_image('run_animation.png')
idle = load_image('character.png')
x = 800 //2
frame = 0
dir = 0
animation_key = 0
running = True

while running:
    clear_canvas()
    grass.draw(400, 30)
    if animation_key == 0:
        idle.draw_now(x,90)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    if x>=800 and dir == 1:
        x = 800
        animation_key = 0
    elif x<=0 and dir == -1:
        x=0
        animation_key = 0
    else:
        x += dir * 5
    delay(0.01)


close_canvas()
