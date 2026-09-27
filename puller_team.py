import time
from pynput.mouse import Button, Controller
from pynput import mouse
import sys
import importlib
import socket

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

# ----- Configuration -----#

resolution = '1920'
pull_weapon = 'F1'
sit_key = 'N'
pull_key = '6'
endu_reg = True
mana_reg = True
role = fight.thane_ae_team
buffcount = 5  #max: 9 buffs
pullcount = 3 #pulls until reg
heal_IP = "192.168.0.42"
team = {"heal": heal_IP}

#--------------------------#

# Variables

buffx = 0
salx = 0
tryx = 0
pullx = 0
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



def send_forget(command, target):
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target, 5000))

    message = command
    client.sendall(message.encode())
    client.close()

def send_wait(command, target):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target, 5000))

    message = command
    client.sendall(message.encode())

    response = client.recv(1024)
    response_dec = response.decode()
    print(response.decode())

    client.close()
    return response_dec   


if __name__ == '__main__':
    if countdown():
        getReady()
    while True:
        if targeting.targeting(pull_key, pull_weapon):
            tryx +=1
            if tryx >= 10:
                sys.exit("0")
            
            elif targeting.pull_check(pull_key, pull_weapon):
                tryx = 0
                for x in team:
                    send_forget('fight', team[x])
                if role(pull_weapon):
                    buffx = buffx + 1
                    pullx = pullx + 1
                    for x in team:
                        send_forget('wait', team[x])
                    print("Buffing in", 20-buffx, "pulls.")
                    if buffx >= 20:
                        buffx = 0
                        for x in team:
                            send_forget('buff', team[x])
                        if regging.buffing(buffcount):
                            regging.regging(sit_key, mana_reg, endu_reg)
                    elif pullx >= pullcount:
                        pullx = 0
                        dik_keys.Press(sit_key)
                        print("|------- TEAM regging -------|")
                        for x in team:
                            print(f"|-- {team[x]}: response: ", send_wait('regg', team[x]), " --|")
                        regging.regging(sit_key, mana_reg, endu_reg)            