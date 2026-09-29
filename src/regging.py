
import time

#local dp
import src.targeting as targeting
import src.dik_keys as dik_keys
import configs.config_priv as conf



def regging(sitkey, endu, mana, stop_event=None):
    print('--------| regging start |---------')
    dik_keys.Press(sitkey)
    endux = endu
    manax = mana
    while True:
        time.sleep(2)
        if targeting.get_px('healthbar', 'red') > conf.healthbarthreshold:
            print('-- Health OK --')
            if not manax or targeting.get_px('manabar', 'green') > conf.current.manabarthreshold:
                print('-- Mana OK --')
                if not endux or targeting.get_px('endubar', 'green') > conf.endubarthreshold:
                    print('-- Endu OK --')
                    time.sleep(2)
                    print('--------| regging done |---------')
                    time.sleep(2)    
                    dik_keys.Press(sitkey)
                    return True

def regging_lead(sitkey):
    print('--------| regging start |---------')
    dik_keys.Press(sitkey)



def buffing(count, stop_event=None):
    print('--------| buffing start |---------')
    x = count
    #go to bar 6
    dik_keys.Combo("SHIFT", "6")
    for i in range(0,x):
        dik_keys.Press(str(i+1))
        time.sleep(3.5)
    #go to bar 1
    time.sleep(1)
    dik_keys.Combo("SHIFT", "5") 
    return True  

def wait(stop_event):
    print('--------| Waiting |---------')
    while not stop_event.is_set():
        time.sleep(3)



def salvage():
    
    dik_keys.Combo("SHIFT", "5") #bar 5
   


