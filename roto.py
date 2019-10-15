import time
import json

from ahk import AHK
from colorama import init, Fore, Back, Style, ansi

init()

ahk = AHK(executable_path='C:\\Program Files\\AutoHotkey\\AutoHotkey.exe')

# ahk.mouse_move(x=100, y=100, blocking=True)  # Blocks until mouse finishes moving (the default)
# ahk.mouse_move(x=150, y=150, speed=10, blocking=True) # Moves the mouse to x, y taking 'speed' seconds to move
# print(ahk.mouse_position)  #  (150, 150)

def rgbToHex(r, g, b):
    print(r, g, b)
    '%02x%02x%02x' % (int(r*255), int(g*255), int(b*255))
    # '#%02x%02x%02x' % (r, g, b)

with open('healing.json') as healing_file:
    data = json.load(healing_file)
    for value in data.values():
        # print(value['colour'][0])
        print(rgbToHex(value['colour'][0], value['colour'][1], value['colour'][2]))

# with open('keys.json') as data_file:    
#     data = json.load(data_file)
#     for value in data.values():
#         print(value['key'], value['image'])

while True:
    ansi.clear_screen()
    time.sleep(0.3)

    shadowguard = ahk.image_search('C:\\Users\\Green\\Desktop\\Roto\\shadowguard.png', upper_bound=(0, 0), lower_bound=(440, 10))

    healing_engine_pixel = ahk.pixel_get_color(442, 0)

    print(healing_engine_pixel)

    if (shadowguard != None): 
        print(Back.GREEN + 'Found shadowguard')
        ahk.send('+e', raw=False)
