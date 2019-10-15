from imagesearch import *

def saveMissingIcon():
    im = region_grabber((19, 0, 37, 11))
    im.save('icon.png')

skills = [
    # Generic
    { "image": "./generic/chat.png", "hotkey": [] },
    { "image": "./generic/eat.png", "hotkey": [] },
    { "image": "./generic/mount.png", "hotkey": [] },
    { "image": "./generic/out_of_combat.png", "hotkey": [] },
    { "image": "./generic/target.png", "hotkey": [] },
    # Classes
    { "image": "./classes/warrior.png", "hotkey": [] },
    # Stance
    { "image": "./warrior/berserker_stance.png", "hotkey": ['alt', 'x'] },
    { "image": "./warrior/battle_stance.png", "hotkey": ['alt', 'x'] },
    # Abilities
    { "image": "./warrior/battle_shout.png", "hotkey": [] },
    { "image": "./warrior/bloodrage.png", "hotkey": [] },
    { "image": "./warrior/execute.png", "hotkey": [] },
    { "image": "./warrior/hamstring.png", "hotkey": [] },
    { "image": "./warrior/mortal_strike.png", "hotkey": [] },
    { "image": "./warrior/whirlwind.png", "hotkey": [] },
    { "image": "./warrior/overpower.png", "hotkey": [] }
]

while True:
    time.sleep(0.1)

    im = region_grabber((0, 0, 400, 11))

    found_match = 0

    # for skill in skills:
    for num, skill in enumerate(skills, start=1):
        match_position = imagesearcharea(skill['image'], 0, 0, 400, 11, 0.8, im)
        if match_position[0] != -1:
            found_match = 1
            print("Found match: ", skill['image'])

        # else:
            # print("Found nothing...")

    if found_match == 0 and num == len(skills):
        print('Log missing icon')
        saveMissingIcon()
    #pyautogui.hotkey('alt', 'x')
    