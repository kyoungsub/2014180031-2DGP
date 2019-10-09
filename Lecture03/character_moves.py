from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
while (1):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(400 + 200 * math.cos(x),  300 + 200 * math.sin(x))
    
    x+=0.1
    
    delay(0.1)

close_canvas()
