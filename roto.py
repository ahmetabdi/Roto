import time
import pyautogui
import cv2

from helpers.imagesearch import region_grabber, imagesearcharea
from helpers.data import targets, abilities

def convertToRgb(array):
    r = '{0:.6f}'.format((array[0] / 255))
    g = '{0:.6f}'.format((array[1] / 255))
    b = '{0:.6f}'.format((array[2] / 255))
    return [float(b), float(g), float(r)]

while True:
    im = region_grabber((442, 0, 443, 1))
    im.save('icon.png')

    image = cv2.imread('icon.png')
    image_colour = convertToRgb(image[0, 0])

    for target in targets:
        if target["colour"] == image_colour:
            print(target["name"])
            pyautogui.hotkey(*target['hotkey'])
    
    # time.sleep(0.1)


# while True:
#     # Fetch top-left bar
#     im = region_grabber((0, 0, 400, 11))

#     found_match = 0

#     for ability in abilities:
#         match_position = imagesearcharea(ability['image'], 0, 0, 400, 11, 0.8, im)
#         # Found ability
#         if match_position[0] != -1:
#             found_match = 1
#             print("Found match: ", ability['image'])
#             # Cast the ability
#             # pyautogui.hotkey(*ability['hotkey'])

#     # if we don't find a match log the icon
#     if found_match == 0:
#         print('Log missing icon')
#         im = region_grabber((19, 0, 37, 11))
#         im.save('icon.png')

#     time.sleep(0.1)
