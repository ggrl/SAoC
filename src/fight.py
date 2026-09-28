import time

#local dp
import configs.UI_config as UI_config
import src.dik_keys as dik_keys
import src.targeting as targeting
import configs.config_priv as conf

#------------------------
# - hunter (solo hunter)
# - thane (solo thane)
# - SM_bomb_team (SM - bomb)
# - healer_ae_team (healer ae pull)
#-------------------------


#Hunter: 3: Standart-Shot, 3: Power-Shot, 2: Speer-Style(anytime) 3: Speer-Style(Follow-up,cond.)  F3: Bogen, F2: Speer
def hunter():
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
            dik_keys.Press('F3')    
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
def thane():
    print('--------| FIGHT rotation |---------')
    castdelay = 3
    meleedelay = 3.5
    time.sleep(.5)
    dik_keys.Press('4')
    time.sleep(.5)
    for x in range(3):
        dik_keys.Press('3')
        time.sleep(castdelay)
    dik_keys.Press('F1')
    time.sleep(.5)
    dik_keys.Press('2')
    time.sleep(.5)
    x = 0
    y = 10
    while True:
        if targeting.get_px('targetbar', 'blue') < 140000 or x >= y:
            dik_keys.Press('2')
            time.sleep(meleedelay)
            dik_keys.Press('F1')    
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

# 3: bomb 0: /assist puller 4: quickcast 5: str/con-debuff
def SM_bomb_team(stop_event):
    castdelay = 2.5
    print("|--- Start Fight ---|")
    #wait for pull
    stop_event.wait(6)
    while not stop_event.is_set():
        print("- BOMB -")
        dik_keys.Press('0')
        time.sleep(.2)
        dik_keys.Press('5')
        time.sleep(.2)
        for x in range(4):
            if stop_event.is_set():
                return
            dik_keys.Press('3')
            time.sleep(castdelay)
        dik_keys.Press('4')
        time.sleep(.5)
        dik_keys.Press('3')
        time.sleep(1)      


# 3: AE-Stun 0: /assist puller 5: Grp-heal
def healer_ae_team(stop_event):
    castdelay = 2.5
    print("|--- Start Fight ---|")
    #wait for pull
    stop_event.wait(5)
    while not stop_event.is_set():
        dik_keys.Press('0')
        time.sleep(.2)
        print("- AE-Stun -")
        dik_keys.Press('3')
        time.sleep(castdelay)
        dik_keys.Press('3')
        time.sleep(.5)
        for x in range(6):
            if stop_event.is_set():
                return
            print("- Healing -")
            healing()
            time.sleep(.2)
        

#Thane: 6: Mjollnir-AE 3: Cast-DD, 4: Insta-DD, 5: Insta-Pbaoe, 2: Melee-Style(anytime) 1: Melee-Style(Follow-up,cond.)  F2: 2h, F1: 1h
def thane_ae_team(stop_event=None):
        print('--------| FIGHT rotation |---------')
        castdelay = 2.5
        meleedelay = 3.5
        
        if stop_event is not None:
            time.sleep(1)
            dik_keys.Press('0')
            time.sleep(.5)
            dik_keys.Press('4')
            time.sleep(.5)
            for x in range(6):
                if stop_event.is_set():
                    return
                dik_keys.Press('0')
                time.sleep(.5)
                dik_keys.Press('6')
                time.sleep(castdelay)
            while not stop_event.is_set():
                dik_keys.Press('5')
                time.sleep(.5)
                dik_keys.Press('1')
                time.sleep(.5)
                dik_keys.Press('2')
                time.sleep(meleedelay)
                dik_keys.Press('0')
                time.sleep(.5)
                dik_keys.Press('4')
                time.sleep(.5)
        else:
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
            y = 5    
            if targeting.get_px('targetbar', 'blue') < 140000 or x >= y:    
                dik_keys.Click(button='left', x=UI_config.scrnx1+UI_config.scrnw//2, y=UI_config.scrny1+UI_config.scrnh//2)
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


'''
def healing():
    grp = targeting.get_px_hh(conf.grp_size)
    under_50 = [i for i, x in enumerate(grp) if x < conf.hhelp50]
    print(sum(x < conf.hhelp100 for x in grp))
    if sum(x < conf.hhelp100 for x in grp) >= conf.grp_size:
        print(sum(x < conf.hhelp100 for x in grp))
        print("grp size: ", conf.grp_size)
        return "-- Everyone Full --"
    
    elif under_50:
        index = under_50[grp.index(max(grp[i] for i in under_50))]
        dik_keys.PoC(getattr(conf, 'target_grp'+str(index+1)))
        time.sleep(.2)
        dik_keys.PoC(conf.singleheal)
        time.sleep(2.5)


    elif sum(x > conf.hhelp100 for x in grp) >= 3:
        time.sleep(.2)
        dik_keys.PoC(conf.grpheal)
        time.sleep(2.4)

    else:
        index = grp.index(max(grp))
        dik_keys.PoC(getattr(conf, 'target_grp'+str(index+1)))
        time.sleep(.2)
        dik_keys.PoC(conf.singleheal)
        time.sleep(2.5) ''' 

def healing():
    grp = targeting.get_px_hh(conf.grp_size)
    # Wenn alle über 97 sind → nichts machen
    if all(x < conf.hhelp100 for x in grp):
        return grp

    # Werte 43-44 ignorieren
    valid = [i for i, x in enumerate(grp) if not conf.hhelpdead <= x <= conf.hhelpdead + 2500]

    # Falls nur ignorierte Werte vorhanden sind
    if not valid:
        return grp

    # Werte unter 50
    under_50 = [i for i in valid if grp[i] > conf.hhelp50]

    if under_50:
        index = max(under_50, key=lambda i: grp[i])
        dik_keys.PoC(getattr(conf, 'target_grp'+str(index+1)))
        time.sleep(.2)
        dik_keys.PoC(conf.singleheal)
        time.sleep(2.5)

    elif sum(x > conf.hhelp100 for x in grp) >= 3:
        time.sleep(.2)
        dik_keys.PoC(conf.grpheal)
        time.sleep(2.4)

    else:
        index = max(valid, key=lambda i: grp[i])
        dik_keys.PoC(getattr(conf, 'target_grp'+str(index+1)))
        time.sleep(.2)
        dik_keys.PoC(conf.singleheal)
        time.sleep(2.5)

    return grp


