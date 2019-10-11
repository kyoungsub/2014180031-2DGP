
from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
frame = 0
p_x, p_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
i, t = 0,0
flag = 0
direction = 1
px,py = [KPU_WIDTH // 2], [KPU_HEIGHT // 2]
for n in range(1,10):
    px.append(random.randint(100, 1000))
    py.append(random.randint(100,900))


while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    if (p_x >= px[flag] and flag<= 8):
        direction = 1        
    elif(p_x < px[flag] and flag <= 8):
        direction = 0
    elif (flag >= 9 and direction == 1):
        direction = 3
    elif (flag >= 9 and direction ==0):
        direction =2



    i = i+1
    t= i/100
    if (flag == 0):
        p_x = (2*t**2-3*t+1)*px[flag]+(-4*t**2+4*t)*px[flag+1]+(2*t**2-t)*px[flag+2]
        p_y = (2*t**2-3*t+1)*py[flag]+(-4*t**2+4*t)*py[flag+1]+(2*t**2-t)*py[flag+2]
    elif (flag == 8):
        p_x = (2*t**2-3*t+1)*px[flag-1]+(-4*t**2+4*t)*px[flag]+(2*t**2-t)*px[flag+1]
        p_y = (2*t**2-3*t+1)*py[flag-1]+(-4*t**2+4*t)*py[flag]+(2*t**2-t)*py[flag+1]
    elif (flag <= 7):
        p_x = ((-t**3 + 2*t**2 - t)*px[flag-1] + (3*t**3 - 5*t**2 + 2)*px[flag] + (-3*t**3 + 4*t**2 + t)*px[flag+1] + (t**3 - t**2)*px[flag+2])/2
        p_y = ((-t**3 + 2*t**2 - t)*py[flag-1] + (3*t**3 - 5*t**2 + 2)*py[flag] + (-3*t**3 + 4*t**2 + t)*py[flag+1] + (t**3 - t**2)*py[flag+2])/2

    if ( flag == 0 and i>= 50):
        i = 0
        flag +=1
    elif ( flag == 7 and i>= 100):
        i = 50
        flag +=1
    elif ( flag <= 8 and i>= 100):
        i=0
        flag +=1

    character.clip_draw(frame * 100, 100 * direction, 100, 100, p_x, p_y)        
    
    update_canvas()

    frame = (frame + 1) % 8
    delay(0.01)

close_canvas()

