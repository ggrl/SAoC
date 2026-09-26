import numpy as np
import cv2
from PIL import ImageGrab as ig
import time

#local dp
import UI_config
import dik_keys
import targeting

#------------------------
# - hunter (solo hunter)
# - thane (solo thane)
# - SM_bomb_team (SM - bomb)
# - healer_ae_team (healer ae pull)
#-------------------------


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

#Thane: 3: Cast-DD, 4: Insta-DD, 5: Insta-Pbaoe, 2: Melee-Style(anytime) 1: Melee-Style(Follow-up,cond.)  F2: 2h, F1: 1h
def thane(pull_weapon):
    print('--------| FIGHT rotation |---------')
    castdelay = 3
    meleedelay = 3.5
    time.sleep(.5)
    dik_keys.Press('4')
    time.sleep(.5)
    for x in range(4):
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

# 3: bomb
def SM_bomb_team(stop_event):
    castdelay = 3
    print("|--- Start Fight ---|")
    #wait for pull
    time.sleep(5)
    while not stop_event.is_set():
        print("- BOMB -")
        dik_keys.Press('3')
        time.sleep(castdelay)
        dik_keys.Press('3')
        time.sleep(castdelay)
        dik_keys.Press('3')

# 3: AE-Stun 0: /assist puller 5: Grp-heal
def healer_ae_team(stop_event):
    castdelay = 3
    print("|--- Start Fight ---|")
    #wait for pull
    time.sleep(6)
    while not stop_event.is_set():
        dik_keys.Press('0')
        time.sleep(.5)
        print("- AE-Stun -")
        dik_keys.Press('3')
        time.sleep(castdelay)
        dik_keys.Press('3')
        time.sleep(castdelay)
        for x in range(3):
            print("- GRP-Heal -")
            dik_keys.Press('5')
            time.sleep(castdelay)
            dik_keys.Press('5')
            time.sleep(6)
        

#Thane: 6: Mjollnir-AE 3: Cast-DD, 4: Insta-DD, 5: Insta-Pbaoe, 2: Melee-Style(anytime) 1: Melee-Style(Follow-up,cond.)  F2: 2h, F1: 1h
def thane_ae_team(pull_weapon):
        print('--------| FIGHT rotation |---------')
        castdelay = 3
        meleedelay = 3.5
        time.sleep(.5)
        dik_keys.Press('4')
        time.sleep(.5)
        for x in range(6):
            dik_keys.Press('6')
            time.sleep(castdelay)
        time.sleep(.5)
        dik_keys.Press('2')
        time.sleep(.5)
        x = 0
        y = 10
        while True:
            if targeting.get_px('targetbar', 'blue') < 200000 or x >= y:    
                print('fight finished')
                return True  
            else:
                dik_keys.Press('5')
                time.sleep(.5)
                dik_keys.Press('1')
                time.sleep(.5)
                dik_keys.Press('2')
                time.sleep(meleedelay)
                dik_keys.Press('TAB')
                time.sleep(.5)
                x = x+1 
                print('Attackloop', x, '/', y)
        
        
