from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global c_x, c_y
    global click_x, click_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            c_x, c_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            click_x, click_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
 

open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor_arrow = load_image('hand_arrow.png')


running = True
c_x, c_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
p_x,p_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
click_x, click_y = 0, 0
frame = 0
i, t = 0,0
direction = 1
hide_cursor()




while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursor_arrow.draw(c_x, c_y)

    if p_x >= click_x:
        direction = 0
    else:
        direction = 1

    i = (i +1) %100
    t= i/100
    p_x = (1-t)* p_x + t * click_x
    p_y = (1-t) * p_y + t* click_y
    character.clip_draw(frame * 100, 100 * direction, 100, 100, p_x, p_y)        
    
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()

