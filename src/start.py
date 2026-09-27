import time

#local dp
import configs.UI_config as UI_config
import src.dik_keys as dik_keys
import src.regging as regging

def hunter(grp_size, buffcount, stop_event=None):
    print('--------| Startup |---------')
    regging.buffing(buffcount)
    return True

#Thane: 3: Cast-DD, 4: Insta-DD, 5: Insta-Pbaoe, 2: Melee-Style(anytime) 1: Melee-Style(Follow-up,cond.)  F2: 2h, F1: 1h
def thane(grp_size, buffcount, stop_event=None):
    print('--------| Startup |---------')
    regging.buffing(buffcount)
    return True

# 3: f6: buffbar (0: cast pet)
def SM_bomb_team(grp_size, buffcount, stop_event=None):
    print('--------| Startup |---------')
    dik_keys.Combo('SHIFT', '6') #go to buffbar
    time.sleep(0.5)
    dik_keys.Press('0') #cast pet
    time.sleep(4)
    regging.buffing(buffcount)
    return True

# 3: AE-Stun 0: /assist puller 5: Grp-heal
def healer_ae_team(grp_size, buffcount, stop_event=None):
    print('--------| Startup |---------')
    regging.buffing(buffcount)
    dik_keys.Combo('SHIFT', '7') #go to buffbar
    time.sleep(0.5)
    for x in range(grp_size):
        #y = 'F'+str(x+7)
        #getattr(dik_keys, 'Press')(y)
        #dik_keys.Press('F'+str(x+7))
        dik_keys.Combo('SHIFT', 'F'+ str(x+1))
        #dik_keys.Press('F7')
        time.sleep(4)
        for x in range(5):
            dik_keys.Press(x+1)
            time.sleep(3.5)
    dik_keys.Combo('SHIFT', '5') #go to fightbar
    return True
        

#Thane: 6: Mjollnir-AE 3: Cast-DD, 4: Insta-DD, 5: Insta-Pbaoe, 2: Melee-Style(anytime) 1: Melee-Style(Follow-up,cond.)  F2: 2h, F1: 1h
def thane_ae_team(grp_size, buffcount, stop_event=None):
    print('--------| Startup |---------')
    regging.buffing(buffcount)
    return True        