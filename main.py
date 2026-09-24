import targeting
import fight
import dik_keys
import time
import regging
from pynput.mouse import Button, Controller
from pynput import mouse

'''
Fight-Bar:5
Buff-Bar: 6
Utility-Bar: 7
'''

# --- Configuration ---#

pull_weapon = 'F1'
sit_key = 'N'
pull_key = '3'
mana_reg = True
endu_reg = True
role = fight.thane
buffcount = 5  #max: 9 buffs

# Variables

buffx = 0
salx = 0

mouse = Controller()

def getReady():
    mouse.position = (310,9)
    time.sleep(0.02)
    mouse.press(Button.left)
    time.sleep(0.05)
    mouse.release(Button.left)
    
    dik_keys.Combo('SHIFT', '5') #go to fight-bar
    time.sleep(.5)
    dik_keys.Press(pull_weapon) #equip pull-weapon
    time.sleep(.5)
    dik_keys.Press(pull_key)
    time.sleep(.5)


if __name__ == '__main__':
    getReady()
    while True:
        if targeting.targeting(pull_key, pull_weapon):
            if targeting.pull_check(pull_key, pull_weapon):
                if role():
                    buffx = buffx + 1
                    print("Buffen in", 20-buffx, "pulls.")
                    if buffx >= 20:
                        buffx = 0
                        if regging.buffing(buffcount):
                            regging.regging(sit_key, mana_reg, endu_reg)
                    else:
                        regging.regging(sit_key, mana_reg, endu_reg)            