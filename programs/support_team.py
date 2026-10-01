import socket
import threading
import time


#local dp
import src.fight as fight
import src.regging as regging
import src.dik_keys as dik_keys
import src.start as start
import configs.config_priv as conf


'''
Fight-Bar:5
Buff-Bar: 6
Utility-Bar: 7
'''

# ------ Configuration ------#

resolution = conf.resolution
pull_weapon = conf.pull_weapon
sit_key = conf.sit_key
pull_key = conf.pull_key
endu = conf.endu
mana = conf.mana
role = conf.role
buffcount = conf.buffcount 
grp_size = conf.grp_size

#-----------------------------#


functions = {
    "fight": (getattr(fight, role),()),
    "regg": (regging.regging, (sit_key, endu, mana)),
    "buff": (regging.buffing, (buffcount,)),
    "wait": (regging.wait, ()),
    "start": (getattr(start, role), (grp_size, buffcount)),
    "stick": (start.stick, ()),
    "spread": (start.spread, ()),
    "sprint": (start.sprint, ()),
    "sit": (start.sit, ()),
    "formation": (start.formation, ())
}


stop_event = None
current_thread = None

    

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

def main():
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
         