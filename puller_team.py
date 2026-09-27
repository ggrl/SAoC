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
import configs.config_priv as conf

'''
Fight-Bar:5
Buff-Bar: 6
Utility-Bar: 7
'''

# ----- Configuration -----#

resolution = conf.resolution
pull_weapon = conf.pull_weapon
sit_key = conf.sit_key
pull_key = conf.pull_key
endu_reg = conf.endu_reg
mana_reg = conf.mana_reg
role = conf.role
buffcount = conf.buffcount
pullcount = conf.pullcount
heal_IP = conf.heal_IP
team = conf.team
grp_size = conf.grp_size

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
    mouse.position = (5,5)
    time.sleep(0.5)
    dik_keys.Click()
    time.sleep(0.5)
    regging.buffing(buffcount)
    for x in team:
        send_wait('start', team[x])
    dik_keys.Combo('SHIFT', '5') #go to fight-bar
    time.sleep(.5)
    dik_keys.Press(pull_weapon) #equip pull-weapon
    time.sleep(.5)
    dik_keys.Press(pull_key)
    time.sleep(.5)



def send_forget(command, target):
    print(f"Sending command '{command}' to {target}.")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target, 5000))

    message = command
    client.sendall(message.encode())
    client.close()

def send_wait(command, target):
    print(f"Sending command '{command}' to {target} and waiting for response.")
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
        if targeting.targeting(pull_key):
            tryx +=1
            if tryx >= 50:
                sys.exit("0")
            
            elif targeting.pull_check(pull_key):
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
                        time.sleep(.5)
                        print("|------- TEAM regging -------|")
                        for x in team:
                            print(f"|-- {team[x]}: response: ", send_wait('regg', team[x]), " --|")
                        dik_keys.Press(sit_key)
                        time.sleep(.5)
                        regging.regging(sit_key, mana_reg, endu_reg)            