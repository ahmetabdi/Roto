import time
import pyautogui

from lib.imagesearch import region_grabber, imagesearcharea
from lib.data import targets, abilities

while True:
    # Fetch top-left bar
    im = region_grabber((0, 0, 400, 11))

    found_match = 0

    for ability in abilities:
        match_position = imagesearcharea(ability['image'], 0, 0, 400, 11, 0.8, im)
        # Found ability
        if match_position[0] != -1:
            found_match = 1
            print("Found match: ", ability['image'])
            # Cast the ability
            # pyautogui.hotkey(*ability['hotkey'])

    # if we don't find a match log the icon
    if found_match == 0:
        print('Log missing icon')
        im = region_grabber((19, 0, 37, 11))
        im.save('icon.png')

    time.sleep(0.1)
