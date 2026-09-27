import time
from pynput.mouse import Button, Controller
from pynput import mouse
import sys
import importlib

#local dep

import configs.UI_config as UI_config
import src.targeting as targeting
import src.fight as fight
import src.dik_keys as dik_keys
import src.regging as regging

'''
Fight-Bar:5
Buff-Bar: 6
Utility-Bar: 7
'''

# --- Configuration ---#

resolution = '1920'
pull_weapon = 'F1'
sit_key = 'N'
pull_key = '3'
mana_reg = True
endu_reg = True
role = fight.thane
buffcount = 3  #max: 9 buffs

#--------------------------#

# Variables

buffx = 0
salx = 0
tryx = 0
UI_config.current = importlib.import_module(f"configs.UI_config_{resolution}")

mouse = Controller()

def countdown():
    cd = 5
    print("|------- Start --------|")
    for i in range(0,cd):
        print(cd-i)
        time.sleep(1.5)
    return True    

def getReady():
    mouse.position = (5,5)
    time.sleep(0.5)
    dik_keys.Click()
    time.sleep(0.5)
    regging.buffing(buffcount)
    dik_keys.Combo('SHIFT', '5') #go to fight-bar
    time.sleep(.5)
    dik_keys.Press(pull_weapon) #equip pull-weapon
    time.sleep(.5)
    dik_keys.Press(pull_key)
    time.sleep(.5)


if __name__ == '__main__':
    if countdown():
        getReady()
    while True:
        if targeting.targeting(pull_key, pull_weapon):
            tryx +=1
            if tryx >= 50:
                sys.exit("0")
            
            elif targeting.pull_check(pull_key, pull_weapon):
                tryx = 0
                if role(pull_weapon):
                    buffx = buffx + 1
                    print("Buffing in", 20-buffx, "pulls.")
                    if buffx >= 20:
                        buffx = 0
                        if regging.buffing(buffcount):
                            regging.regging(sit_key, mana_reg, endu_reg)
                    else:
                        regging.regging(sit_key, mana_reg, endu_reg)            