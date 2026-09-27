import socket
import threading
import time
import importlib


#local dp
import configs.UI_config as UI_config
import src.fight as fight
import src.regging as regging
import src.dik_keys as dik_keys
import src.start as start

'''
Fight-Bar:5
Buff-Bar: 6
Utility-Bar: 7
'''

# ------ Configuration ------#

resolution = '1366VM'
pull_weapon = 'F1'
sit_key = 'N'
pull_key = '3'
endu = False #need endu?
mana = True #need mana?
role = 'healer_ae_team'
buffcount = 3  #max: 9 buffs
grp_size = 3

#-----------------------------#


functions = {
    "fight": (getattr(fight, role),()),
    "regg": (regging.regging,(sit_key, endu, mana)),
    "buff": (regging.buffing,(buffcount,)),
    "wait": (regging.wait,()),
    "start": (getattr(start, role),(grp_size,))
}


UI_config.current = importlib.import_module(f"configs.UI_config_{resolution}")
current_thread = None
stop_event = None


def start_up():
    print("|--- Start Up ---|")
    

def start_worker(command):
    global current_thread, stop_event

    # aktuellen Worker stoppen
    if current_thread and current_thread.is_alive():
        stop_event.set()
        current_thread.join()

    stop_event = threading.Event()
    function, args = functions[command]
    current_thread = threading.Thread(
        target=function,
        args=(*args, stop_event)
    )

    current_thread.start()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("0.0.0.0", 5000))
server.listen(5)

print("|--------- Listening --------|")


while True:

    conn, addr = server.accept()

    try:
        command = conn.recv(1024).decode().strip()

        if command in functions:

            if command =='regg' or command =='start':

                # stop current worker
                if current_thread and current_thread.is_alive():
                        stop_event.set()
                        current_thread.join()
                
                # regging execute synchonous
                functions[command][0](*functions[command][1])
                
                # send client
                conn.sendall(b"DONE")
            else:
                start_worker(command)
        else:
            conn.sendall(b"UNKOWN")

    finally:
        conn.close()