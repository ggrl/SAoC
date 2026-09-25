import numpy as np
import cv2
from PIL import ImageGrab as ig
import time

#local dp
import UI_config
import dik_keys
import targeting


#Hunter: 3: Standart-Shot, 3: Power-Shot, 2: Speer-Style(anytime) 3: Speer-Style(Follow-up,cond.)  F3: Bogen, F2: Speer
def hunter(pull_weapon):
    print('--------| FIGHT rotation |---------')
    bowdelay = 4.5
    meleedelay = 3.5
    time.sleep(.5)
    dik_keys.Press('4')
    time.sleep(bowdelay)
    dik_keys.Press('3')
    time.sleep(bowdelay)
    dik_keys.Press('3')
    time.sleep(bowdelay)
    dik_keys.Press('3')
    time.sleep(bowdelay)
    dik_keys.Press('F2')
    time.sleep(.5)
    dik_keys.Press('2')
    time.sleep(.5)
    x = 0
    while True:
        if targeting.get_px('targetbar', 'red') > 300000:
            #equip bow
            dik_keys.Press(pull_weapon)    
            print('fight beendet')
            return True  
        else:
            dik_keys.Press('1')
            time.sleep(.5)
            dik_keys.Press('2')
            time.sleep(meleedelay)
            x = x+1 
            print(x)

#Thane: 3: Cast-DD, 4: Insta-DD, 5: Insta-Pbaoe, 2: Melee-Style(anytime) 3: Melee-Style(Follow-up,cond.)  F2: 2h, F1: 1h
def thane(pull_weapon):
    print('--------| FIGHT rotation |---------')
    castdelay = 3
    meleedelay = 3.5
    time.sleep(.5)
    dik_keys.Press('4')
    time.sleep(.5)
    dik_keys.Press('3')
    time.sleep(castdelay)
    dik_keys.Press('3')
    time.sleep(castdelay)
    dik_keys.Press('3')
    time.sleep(castdelay)
    dik_keys.Press('3')
    time.sleep(castdelay)
    dik_keys.Press('F1')
    time.sleep(.5)
    dik_keys.Press('2')
    time.sleep(.5)
    x = 0
    y = 10
    while True:
        if targeting.get_px('targetbar', 'blue') < 200000 or x >= y:
            dik_keys.Press(pull_weapon)    
            print('fight finished')
            return True  
        else:
            dik_keys.Press('5')
            time.sleep(.5)
            dik_keys.Press('1')
            time.sleep(.5)
            dik_keys.Press('2')
            time.sleep(meleedelay)
            x = x+1 
            print('Attackloop', x, '/', y)

        
