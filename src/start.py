import time

#local dp
import configs.UI_config as UI_config
import src.dik_keys as dik_keys

def hunter(pull_weapon):
    print('--------| Startup |---------')


#Thane: 3: Cast-DD, 4: Insta-DD, 5: Insta-Pbaoe, 2: Melee-Style(anytime) 1: Melee-Style(Follow-up,cond.)  F2: 2h, F1: 1h
def thane(pull_weapon):
    print('--------| Startup |---------')
    

# 3: bomb 0: /assist puller 4: quickcast 5: str/con-debuff
def SM_bomb_team(stop_event):
    print('--------| Startup |---------')

# 3: AE-Stun 0: /assist puller 5: Grp-heal
def healer_ae_team(grp_size, stop_event=None):
    print('--------| Startup |---------')
    for x in range(grp_size):
        y = 'F'+str(x+7)
        getattr(dik_keys, 'Press')(y)
        dik_keys.Combo('SHIFT', '7') #go to buffbar
        for x in range(5):
            dik_keys.Press(x+1)
            time.sleep(.5)

        

#Thane: 6: Mjollnir-AE 3: Cast-DD, 4: Insta-DD, 5: Insta-Pbaoe, 2: Melee-Style(anytime) 1: Melee-Style(Follow-up,cond.)  F2: 2h, F1: 1h
def thane_ae_team(pull_weapon):
    print('--------| Startup |---------')        