import numpy as np
import matplotlib.pyplot as plt


with open('input.txt') as f:
    register = [line for line in f.read().split('\n') if line]


oled_ultra_hd = np.zeros((6,40))

def render_pixel(cycle, sprite_pos, display):
    pixel_row = cycle // 40
    pixel_col = cycle % 40

    if abs(sprite_pos - pixel_col) < 2:
        display[pixel_row, pixel_col] = 1

    else:
        display[pixel_row, pixel_col] = 0




    return display



total_stength = 0
x = 1
c = 0

for line in register:    
    words = line.split()
    if words[0] == 'noop':
        render_pixel(c, x, oled_ultra_hd)
        c += 1
        if c in [20, 60, 100, 140, 180, 220]:
            total_stength += x*c

        
        print(oled_ultra_hd)

    elif words[0] == 'addx':
        render_pixel(c, x, oled_ultra_hd)
        c += 1
        if c in [20, 60, 100, 140, 180, 220]:
            total_stength += x*c
        
        render_pixel(c, x, oled_ultra_hd)
        c += 1        
        if c in [20, 60, 100, 140, 180, 220]:
            total_stength += x*c        

        x += int(words[1])

print(total_stength)
plt.imshow(oled_ultra_hd)
plt.show()












            



        





