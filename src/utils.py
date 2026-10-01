import random
import time

#local dp
import src.dik_keys as dik_keys
import configs.config_priv as conf

#--------------- utils ---------------#
def type(text):
    dik_keys.Press('ENTER')
    time.sleep(0.2)
    for char in text:
        print(char)
        dik_keys.Press(char)
        time.sleep(0.1)
    dik_keys.Press('ENTER')  

#----------- Multiteam:

def stick(stop_event=None):
    print('--------| Sticking |---------')
    dik_keys.Combo('SHIFT', 'F1')
    time.sleep(.5)
    dik_keys.Press('F')
    time.sleep(.5)


def spread(stop_event=None):
    print('--------| Spreading |---------')
    key = random.choice(['A','D'])
    delay = random.random()
    print(delay)
    dik_keys.Press(key, delay/2)
    time.sleep(.5)
    delay = random.random()
    dik_keys.Press('S',delay/2)
    key = random.choice(['A','D'])
    delay = random.random()
    dik_keys.Press(key, delay/2)

def formation(stop_event=None):
    print('--------| Formation |---------')
    if conf.role == 'bomb_ae_team':
        dik_keys.Press('W',0.5)
    elif conf.role == 'healer_ae_team':
        dik_keys.Press('D',0.4)      
        time.sleep(.5)
        dik_keys.Press('S',0.8)      
        time.sleep(.5)
    elif conf.role == 'thane_ae_team':
            dik_keys.Press('A',0.5)      
            time.sleep(.5)
            dik_keys.Press('S',0.6)      
            time.sleep(.5)
    else:
        spread()            

def sprint(stop_event=None):
    print('--------| Sprinting |---------') 
    dik_keys.Press(conf.sprint_key) 

def sit(stop_event=None):
    print('--------| Sit down |---------') 
    dik_keys.Press(conf.sit_key)

def quit(stop_event=None):
    print('--------| Quit |---------') 
    type('quit')  

  