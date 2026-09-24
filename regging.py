import dik_keys
import time
import UI_config
import numpy as np
import cv2
from PIL import ImageGrab as ig
import targeting

def regging(sitkey, endu, mana):
    print('--------| regging start |---------')
    regx = 1
    dik_keys.Press(sitkey)
    endux = endu
    manax = mana
    while True:
        time.sleep(2)
        if targeting.get_px('healthbar', 'red') > 150000:
            if not manax or targeting.get_px('manabar', 'green') > 140000:
                if not endux or targeting.get_px('endubar', 'green') > 45000:
                    time.sleep(2)
                    print('--------| regging done |---------')
                    time.sleep(2)    
                    dik_keys.Press(sitkey)
                    return True

def buffing(count):
    print('--------| buffing start |---------')
    x = count
    #go to bar 7
    dik_keys.Combo("SHIFT", "6")
    for i in range(0,x):
        dik_keys.Press(str(i+1))
        time.sleep(3.5)
    #go to bar 1
    time.sleep(1)
    dik_keys.Combo("SHIFT", "5") 
    return True  


def salvage():
    
    dik_keys.Combo("SHIFT", "5") #bar 5
   


